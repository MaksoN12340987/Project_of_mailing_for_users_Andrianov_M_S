from django.urls import path

from .views import (
    MainView,
    Create,
    Update,
    Detail,
    MessageCreate,
    MessageUpdate,
    MessageDetail,
    AttemptSendCreate,
    AttemptSendUpdate,
    AttemptSendDetail,
)
from .apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    
    path("create_newsletter/", Create.as_view(), name="create"),
    path("update_newsletter/<int:pk>/", Update.as_view(), name="update"),
    path("newsletter/<int:pk>/", Detail.as_view(), name="newsletter"),
    
    path("create_message/", MessageCreate.as_view(), name="create_message"),
    path("update_message/<int:pk>/", MessageUpdate.as_view(), name="update_message"),
    path("message/<int:pk>/", MessageDetail.as_view(), name="message"),
    
    path("attemptsend/", AttemptSendDetail.as_view(), name="attemptsend_list"),
    path("create_attempt/", AttemptSendCreate.as_view(), name="create_attempt"),
    path("update_attempt/<int:pk>/", AttemptSendUpdate.as_view(), name="update_attempt"),
    path("attemptsend/<int:pk>/", AttemptSendDetail.as_view(), name="attemptsend"),
]
