from django.urls import path

from .views import (
    MainView,
    MessagesView,
    MessageCreate,
    MessageUpdate,
    MessageDetail,
    NewsletterCreate,
    NewsletterUpdate,
    NewsletterDetail,
    AttemptSendCreate,
    AttemptSendUpdate,
    AttemptSendDetail,
    AttemptSendList
)
from .apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
# New class
# Message
    path("list_message/", MessagesView.as_view(), name="list_message"),
    path("create_message/", MessageCreate.as_view(), name="create_message"),
    path("update_message/<int:pk>/", MessageUpdate.as_view(), name="update_message"),
    path("message/<int:pk>/", MessageDetail.as_view(), name="message"),
    path("del_message/<int:pk>/", MessageDetail.as_view(), name="del_message"),
# New class
# Newsletter
    path("create_newsletter/", NewsletterCreate.as_view(), name="create"),
    path("update_newsletter/<int:pk>/", NewsletterUpdate.as_view(), name="update"),
    path("newsletter/<int:pk>/", NewsletterDetail.as_view(), name="newsletter"),
    path("del_newsletter/<int:pk>/", NewsletterDetail.as_view(), name="del_newsletter"),
# New class
# AttemptSend
    path("create_attempt/", AttemptSendCreate.as_view(), name="create_attempt"),
    path("attemptsend_list/", AttemptSendList.as_view(), name="attemptsend_list"),
    path("update_attempt/<int:pk>/", AttemptSendUpdate.as_view(), name="update_attempt"),
    path("attemptsend/<int:pk>/", AttemptSendDetail.as_view(), name="attemptsend"),
    path("del_attemptsend/<int:pk>/", AttemptSendDetail.as_view(), name="del_attemptsend"),
]
