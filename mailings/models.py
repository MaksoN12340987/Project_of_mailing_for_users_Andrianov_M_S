from django.db import models

from users.models import MailingRecipient


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name="Тема", unique=True)
    content = models.TextField(max_length=200, verbose_name="Содержание")
    attached_file = models.ImageField(
        upload_to="newsletter/",
        verbose_name="Прикрепленные файлы",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["subject"]


class Newsletter(models.Model):
    STATUS_CHOICES = [
        ("Created", "event created"),
        ("Started", "event started"),
        ("Completed", "event completed"),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES, default="Created", verbose_name="Категория"
    )

    first_sending = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время первой отправки"
    )
    сompletion_time = models.DateTimeField(
        default=None,
        null=True,
        verbose_name="Дата и время окончания отправки",
        blank=True,
        auto_created=True,
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Содержание рассылки"
    )
    recipients = models.ManyToManyField(
        MailingRecipient, verbose_name="Получатели рассылки"
    )

    def __str__(self):
        return f"{self.message}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["status"]
        permissions = [("mailing_manager", "Mailing list manager")]


class AttemptSend(models.Model):
    STATUS = [
        ("Not_start", "Did not start"),
        ("Not_successful", "event started"),
        ("Successful", "event completed"),
    ]
    status = models.CharField(
        choices=STATUS, default="Not_start", verbose_name="Статус попытки"
    )
    time_attempt = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время попытки"
    )
    mail_server_response = models.CharField(
        default="Нет ответа", verbose_name="Ответ почтового сервера", null=True
    )
    news_letter = models.ForeignKey(
        Newsletter, on_delete=models.CASCADE, verbose_name="Содержание рассылки"
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попыток рассылки"
        ordering = ["status"]
