from typing import Any

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from users.models import MailingRecipient


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        product_moderator = Group.objects.create(name="Product moderator")

