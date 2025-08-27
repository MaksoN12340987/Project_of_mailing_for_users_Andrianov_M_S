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
        return f"{self.subject}"

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
        default=None, null=True, verbose_name="Дата и время окончания отправки"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Содержание рассылки"
    )
    recipients = models.ManyToManyField(
        MailingRecipient, verbose_name="Получатели рассылки"
    )

    def __str__(self):
        return f"{self.recipients} {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["email"]
        permissions = [("mailing_manager", "Mailing list manager")]
