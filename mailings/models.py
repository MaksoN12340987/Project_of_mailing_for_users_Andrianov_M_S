from django.db import models

from users.models import MailingRecipient


class Newsletter(models.Model):
    STATUS_CHOICES = [
        ("inform", "information"),
        ("automatic", "automatic"),
        ("special", "special"),
    ]
    categories = models.CharField(
        choices=STATUS_CHOICES, default="automatic", verbose_name="Категория"
    )

    email = models.ForeignKey(
        MailingRecipient,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )
    name_surname = models.CharField(max_length=200, verbose_name="Ф. И. О.")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
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
