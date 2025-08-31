from typing import Any
from django import forms

from .models import Newsletter, Message, AttemptSend


class CreateMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "subject",
            "content",
            "attached_file",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["subject"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Тема сообщения",
            }
        )
        self.fields["content"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Содержание сообщения ",
            }
        )
        self.fields["attached_file"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Дополнительны файлы ",
            }
        )


class CreateNewsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            "message",
            "recipients",
            "сompletion_time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["message"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Введите ",
            }
        )
        self.fields["recipients"].widget.attrs.update({"class": "form-select-M"})
        self.fields["сompletion_time"].widget.attrs.update(
            {
                "class": "form-select-M",
            }
        )


class UpdateNewsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            "message",
            "recipients",
            "сompletion_time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["message"].widget.attrs.update(
            {
                "class": "form-control-M",
                "placeholder": "Введите ",
            }
        )
        self.fields["сompletion_time"].widget.attrs.update(
            {
                "class": "form-control-M",
            }
        )
        self.fields["recipients"].widget.attrs.update({"class": "form-select-M"})


class Attempt_send_form(forms.ModelForm):
    class Meta:
        model = AttemptSend
        fields = [
            "status",
            "news_letter",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["status"].widget.attrs.update(
            {
                "class": "form-select-M",
                "placeholder": "Тема сообщения",
            }
        )
        self.fields["news_letter"].widget.attrs.update(
            {
                "class": "form-select-M",
                "placeholder": "Содержание сообщения ",
            }
        )
