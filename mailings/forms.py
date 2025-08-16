from django import forms

from .models import Newsletter


class CreateNewsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            "email",
            "name_surname",
            "content",
            "categories",
            "attached_file",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                "class": "contact-form",
                "placeholder": "Введите",
            }
        )
        self.fields["name_surname"].widget.attrs.update(
            {
                "class": "contact-form",
                "placeholder": "Введите",
            }
        )
        self.fields["content"].widget.attrs.update({"class": "contact-form"})
        self.fields["categories"].widget.attrs.update({"class": "form-select"})
        self.fields["attached_file"].widget.attrs.update({"class": "img"})



class UpdateNewsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            "email",
            "name_surname",
            "content",
            "categories",
            "attached_file",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                "class": "contact-form",
                "placeholder": "Введите",
            }
        )
        self.fields["name_surname"].widget.attrs.update(
            {
                "class": "contact-form",
                "placeholder": "Введите",
            }
        )
        self.fields["content"].widget.attrs.update({"class": "contact-form"})
        self.fields["categories"].widget.attrs.update({"class": "form-select"})
        self.fields["attached_file"].widget.attrs.update({"class": "img"})
