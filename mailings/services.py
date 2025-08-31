import logging

from email.mime.image import MIMEImage
from functools import lru_cache
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail import EmailMultiAlternatives

log_service = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
log_service.addHandler(file_handler)
log_service.setLevel(logging.INFO)


class SendingMessagesEmail:
    newsletter = None
    
    def __init__(self, newsletter) -> None:
        self.newsletter = newsletter
        self.path_to_image = f'media/{newsletter.message.attached_file}'
        self.list_emails = self.__validation()
        self.message = ""
    
    def __validation(self):
        result = []
        for i, value in enumerate(self.newsletter.recipients.all()): # type: ignore
            result.append(value.email)
        
        return result

    @lru_cache()
    def __logo_data(self, path_to_image: str):
        log_service.info(path_to_image)
        logo = None
        
        try:
            with open(path_to_image, 'rb') as f:
                logo_data = f.read()
                logo = MIMEImage(logo_data)
                logo.add_header('Content-ID', '<image>')
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        
        return logo

    def __create_message(self, email, path_to_image: str):
        
        subject = f"{self.newsletter.message.subject}" # type: ignore
        content = f"""
        <html>
            <body>
                <p>{self.newsletter.message.content}</p>
                <br>
                <img src="cid:image" tabindex='0'>
            </body>
        </html>
        """
        transmitter = "gorscheneow2018@yandex.ru"
        
        message = EmailMultiAlternatives(
            subject,
            content,
            transmitter,
            to=[email]
        )
        log_service.info(f"message: {message}")
        
        message.mixed_subtype = 'related'
        message.attach_alternative(content, "text/html")
        try:
            message.attach(self.__logo_data(path_to_image)) # type: ignore
        except ValueError:
            pass

        return message.send(fail_silently=False)
    
    def attempt_send(self):
        list_responce = []
        for i, value in enumerate(self.list_emails):
            list_responce.append(self.__create_message(value, self.path_to_image))
        
        log_service.info(f"Результат отправки: {list_responce}")
        for responce in list_responce:
            if not responce:
                return 0
        
        return 1
