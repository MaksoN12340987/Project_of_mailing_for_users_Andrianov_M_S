from django.db import models

from users.models import MailingRecipient


class Newsletter(models.Model):
    STATUS_CHOICES = [
        ("Created", "event created"),
        ("Started", "event started"),
        ("Completed", "event completed"),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES, default="automatic", verbose_name="Категория"
    )
    
    first_sending = models.DateTimeField(auto_now_add=True)
    сompletion_time = models.DateTimeField(default=None, null=True)

    email = models.ForeignKey(
        MailingRecipient,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )
    recipients = models.CharField(max_length=200, verbose_name="Ф. И. О.")
    title = models.CharField(max_length=200, verbose_name="Тема", null=True)
    message = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    attached_file = models.ImageField(
        upload_to="newsletter/", verbose_name="Доп файлы", blank=True, null=True
    )

    def __str__(self):
        return f"{self.email} {self.name_surname}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["email"]
        permissions = [("mailing_manager", "Mailing list manager")]
