from django.urls import path

from .views import MainView, Create, Update, Detail
from .apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("create/", Create.as_view(), name="create"),
    path("update/<int:pk>/", Update.as_view(), name="update"),
    path("newsletter/<int:pk>/", Detail.as_view(), name="newsletter"),
]
