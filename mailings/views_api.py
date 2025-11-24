from rest_framework import generics

from .models import AttemptSend, Message, Newsletter
from .serializers import AttemptSendSerializer, MessageSerializer, NewsletterSerializer


# Message API views
class MessageListAPI(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


# Newsletter API views
class NewsletterListAPI(generics.ListAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()


# AttemptSend API views
class AttemptSendListAPI(generics.ListAPIView):
    serializer_class = AttemptSendSerializer
    queryset = AttemptSend.objects.all()


class AttemptSendRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = AttemptSendSerializer
    queryset = AttemptSend.objects.all()


class AttemptSendUpdateAPI(generics.UpdateAPIView):
    serializer_class = AttemptSendSerializer
    queryset = AttemptSend.objects.all()


class AttemptSendCreateAPI(generics.CreateAPIView):
    serializer_class = AttemptSendSerializer


class AttemptSendDestroyAPI(generics.DestroyAPIView):
    serializer_class = AttemptSendSerializer
    queryset = AttemptSend.objects.all()
