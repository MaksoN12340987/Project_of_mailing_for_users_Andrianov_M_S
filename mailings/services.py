import logging

from django.db.models import Model

from email.mime.image import MIMEImage
from functools import lru_cache
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail import EmailMultiAlternatives

from config.settings import EMAIL_HOST_USER

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
    newsletter: Model

    def __init__(self, newsletter) -> None:
        self.newsletter = newsletter
        self.path_to_image = f"media/{newsletter.message.attached_file}"
        self.list_emails = self.__validation()
        self.message = ""

    def __validation(self) -> list[str]:
        """Метод преобразует множество в список строк с
        почтовыми адресами получатеелй

        Returns:
            _type_: _description_
        """
        result = []
        for i, value in enumerate(self.newsletter.recipients.all()):  # type: ignore
            result.append(value.email)

        return result

    @lru_cache()
    def __logo_data(self, path_to_image: str) -> MIMEImage:
        """Метод подготовки изображения
        к приереплению в шаблон

        Args:
            path_to_image (str): путь до изображения

        Returns:
            MIMEImage: обьект строкового представлеия
                        изображения
        """
        log_service.info(path_to_image)
        logo = None

        try:
            with open(path_to_image, "rb") as f:
                logo_data = f.read()
                logo = MIMEImage(logo_data)
                logo.add_header("Content-ID", "<image>")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

        return logo  # type: ignore

    def __create_message(self, email: str, path_to_image: str) -> int:
        """Метод создает шаблон письма, добавляет изображение,
        если оно загружено, и отправляет на переданный имейл

        Args:
            email (str): емейл получателя
            path_to_image (str): путь до изображения

        Returns:
            _int_: Число, где 1 - успешно отправлено
        """
        subject = self.newsletter.message.subject  # type: ignore
        message = self.newsletter.message.content  # type: ignore
        content = f"""
        <html>
            <body>
                <p>{message}</p>
                <br>
                <img src="cid:image" tabindex='0'>
            </body>
        </html>
        """
        transmitter = EMAIL_HOST_USER

        message = EmailMultiAlternatives(subject, content, transmitter, to=[email])
        log_service.info(f"message: {message}")

        message.mixed_subtype = "related"
        message.attach_alternative(content, "text/html")
        try:
            message.attach(self.__logo_data(path_to_image))  # type: ignore
        except ValueError:
            pass

        return message.send(fail_silently=False)

    def attempt_send(self) -> int:
        """Метод запускает отправки сообщений по переданным
        почтовым адресам

        Returns:
            _int_: 1 - успешно отправено
                   2 - не отправлено
        """
        list_responce = []
        for i, value in enumerate(self.list_emails):
            list_responce.append(self.__create_message(value, self.path_to_image))

        log_service.info(f"Результат отправки: {list_responce}")
        for responce in list_responce:
            if not responce:
                return 0

        return 1
