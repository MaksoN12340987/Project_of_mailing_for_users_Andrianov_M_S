import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from users.models import MailingRecipient

from .forms import CreateNewsletter, UpdateNewsletter, CreateMessage, Attempt_send_form
from .models import Newsletter, Message, AttemptSend

from .services import SendingMessagesEmail

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


# Main
class MainView(ListView):
    model = Newsletter
    template_name = "mailings/main.html"
    context_object_name = "newsletters"

    def get_queryset(self):
        queryset = cache.get("ProductListView_queryset")
        if not queryset:
            queryset = super().get_queryset()
        #     cache.set("authors_queryset", queryset, 60 * 15)
        return queryset

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        context["total_rvsslinks"] = len(Newsletter.objects.all())
        context["active_rvsslinks"] = len(Newsletter.objects.filter(status="Started"))
        context["total_recipients"] = len(MailingRecipient.objects.all())

        logger_views.info(f"{context}".replace(",", "\n"))
        return context


# New class
# Message
class MessagesView(ListView):
    model = Message
    template_name = "mailings/messages.html"
    context_object_name = "messages"
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        logger_views.info(f"{context}".replace(",", "\n"))
        return context


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    form_class = CreateMessage
    template_name = "mailings/create.html"
    context_object_name = "message"
    success_url = reverse_lazy("mailings:main")
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form_valid = super().form_valid(form)
        logger_views.info(form_valid)
        return form_valid


class MessageUpdate(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = CreateMessage
    context_object_name = "message"
    template_name = "mailings/create.html"
    success_url = reverse_lazy("mailings:main")
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form_valid = super().form_valid(form)
        logger_views.info(form_valid)
        return form_valid


class MessageDetail(DetailView):
    model = Message
    context_object_name = "message"
    template_name = "mailings/detail.html"
    success_url = reverse_lazy("mailings:main")


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    context_object_name = "message"
    template_name = "mailings/delete.html"
    success_url = reverse_lazy("mailings:main")


# New class
# Newsletter
class NewsletterCreate(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = CreateNewsletter
    template_name = "mailings/create.html"
    context_object_name = "newsletter"
    success_url = reverse_lazy("mailings:main")


class NewsletterUpdate(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = UpdateNewsletter
    template_name = "mailings/create.html"
    context_object_name = "newsletter"


class NewsletterDetail(DetailView):
    model = Newsletter
    template_name = "mailings/detail.html"
    context_object_name = "newsletter"
    success_url = reverse_lazy("mailings:main")


class NewsletterDelete(DeleteView):
    model = Newsletter
    context_object_name = "newsletter"
    template_name = "mailings/delete.html"
    success_url = reverse_lazy("mailings:main")


# New class
# AttemptSend
class AttemptSendList(ListView):
    model = AttemptSend
    template_name = "mailings/attemptsend_list.html"
    context_object_name = "attemptsends"

    def get_queryset(self):
        queryset = cache.get("ProductListView_queryset")
        if not queryset:
            queryset = super().get_queryset()
        #     cache.set("authors_queryset", queryset, 60 * 15)
        return queryset


class AttemptSendCreate(LoginRequiredMixin, CreateView):
    model = AttemptSend
    form_class = Attempt_send_form
    template_name = "mailings/create_attempt_send.html"
    context_object_name = "attemptsend"
    success_url = reverse_lazy("mailings:main")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        attemptsend = form.save(commit=False)

        newsletter_pk = attemptsend.news_letter.pk
        newsletter = Newsletter.objects.get(pk=newsletter_pk)
        newsletter.status = "Started"
        newsletter.save()

        sending_messages = SendingMessagesEmail(attemptsend.news_letter)
        result = sending_messages.attempt_send()
        logger_views.info(result)

        if result:
            attemptsend.status = "Successful"
            attemptsend.mail_server_response = "Успешно"
        else:
            attemptsend.status = "Not_successful"

        attemptsend.save()

        return super().form_valid(form)
