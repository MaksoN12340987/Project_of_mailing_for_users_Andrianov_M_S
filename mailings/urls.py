from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import MailingsConfig
from .views import (
    AttemptSendCreate,
    AttemptSendList,
    MainView,
    MessageCreate,
    MessageDetail,
    MessagesView,
    MessageUpdate,
    NewsletterCreate,
    NewsletterDetail,
    NewsletterUpdate,
)
from .views_api import (
    MessageListAPI,
    NewsletterListAPI,
    AttemptSendCreateAPI,
    AttemptSendDestroyAPI,
    AttemptSendListAPI,
    AttemptSendRetrieveAPI,
    AttemptSendUpdateAPI,
)

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
    path("create_newsletter/", NewsletterCreate.as_view(), name="create_newsletter"),
    path(
        "update_newsletter/<int:pk>/",
        NewsletterUpdate.as_view(),
        name="update_newsletter",
    ),
    path("newsletter/<int:pk>/", NewsletterDetail.as_view(), name="newsletter"),
    path("del_newsletter/<int:pk>/", NewsletterDetail.as_view(), name="del_newsletter"),
    # New class
    # AttemptSend
    path("create_attempt/", AttemptSendCreate.as_view(), name="create_attempt"),
    path("attemptsend_list/", AttemptSendList.as_view(), name="attemptsend_list"),
    # API message
    path("api/messages/", MessageListAPI.as_view(), name="api_message"),
    # API newsletters
    path("api/newsletters/", NewsletterListAPI.as_view(), name="api_newsletters"),
    # API attempt_send
    path("api/api_sends/", AttemptSendListAPI.as_view(), name="api_sends"),
    path("api/create_api_send/", AttemptSendCreateAPI.as_view(), name="create_api_send"),
    path("api/del_api_send/<int:pk>/", AttemptSendDestroyAPI.as_view(), name="del_api_send"),
    path("api/update_api_send/<int:pk>/", AttemptSendUpdateAPI.as_view(), name="update_api_send"),
    path("api/detail_api_send/<int:pk>/", AttemptSendRetrieveAPI.as_view(), name="detail_api_send"),
]
