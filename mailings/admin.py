from django.contrib import admin  # type: ignore

from .models import Message, AttemptSend, Newsletter


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "content",
        "attached_file",
    )
    search_fields = ("subject",)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "first_sending",
        "сompletion_time",
    )
    list_filter = (
        "status",
        "first_sending",
    )
    search_fields = ("message",)

@admin.register(AttemptSend)
class AttemptSendAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "time_attempt",
        "mail_server_response",
    )
    list_filter = (
        "status",
        "mail_server_response",
    )
    search_fields = ("news_letter",)
