from typing import Any

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from users.models import BaseUser


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        product_moderator = Group.objects.create(name="Product moderator")

        delete_product_permission = Permission.objects.get(codename="delete_product")
        can_unpublish_product_permission = Permission.objects.get(codename="can_unpublish_product")

        product_moderator.permissions.add(delete_product_permission, can_unpublish_product_permission)
        product_moderator.save()

        user = BaseUser.objects.get(pk=2)
        user.groups.add(product_moderator)

        user.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created admin user with email {user.email}"))
