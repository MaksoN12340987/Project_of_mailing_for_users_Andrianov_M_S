from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from mailings.apps import MailingsConfig
from users.apps import UsersConfig
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        f"{MailingsConfig.name}/",
        include(f"{MailingsConfig.name}.urls", namespace=f"{MailingsConfig.name}"),
    ),
    path(
        f"{UsersConfig.name}/",
        include(f"{UsersConfig.name}.urls", namespace=f"{UsersConfig.name}"),
    ),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
