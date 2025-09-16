from rest_framework import serializers

from .models import AttemptSend, Message, Newsletter


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["pk", "status", "first_sending", "сompletion_time"]


class AttemptSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttemptSend
        fields = "__all__"
