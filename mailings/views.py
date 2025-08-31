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


class MainView(ListView):
    model = Newsletter
    template_name = "mailings/main.html"
    context_object_name = "newsletters"


class Create(CreateView):
    model = Newsletter
    form_class = CreateNewsletter
    template_name = "mailings/create.html"
    context_object_name = "newsletter"
    success_url = reverse_lazy("mailings:main")


class Update(UpdateView):
    model = Newsletter
    form_class = UpdateNewsletter
    template_name = "mailings/create.html"
    context_object_name = "newsletter"


class Detail(DetailView):
    model = Newsletter
    template_name = "mailings/detail.html"
    context_object_name = "newsletter"


class MessageCreate(CreateView):
    model = Message
    form_class = CreateMessage
    template_name = "mailings/create.html"
    context_object_name = "message"
    success_url = reverse_lazy("mailings:main")


class MessageUpdate(UpdateView):
    model = Message
    form_class = CreateMessage
    template_name = "mailings/create.html"
    context_object_name = "message"


class MessageDetail(DetailView):
    model = Message
    template_name = "mailings/detail.html"
    context_object_name = "message"


class AttemptSendCreate(CreateView):
    model = AttemptSend
    form_class = Attempt_send_form
    template_name = "mailings/create.html"
    context_object_name = "attemptsend"
    success_url = reverse_lazy("mailings:main")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        attemptsend = form.save(commit=False)
        
        sending_messages = SendingMessagesEmail(attemptsend.news_letter)
        result = sending_messages.attempt_send()
        logger_views.info(result)
        newsletter_pk = attemptsend.news_letter.pk
        
        newsletter = Newsletter.objects.filter(pk=newsletter_pk)[0]
        newsletter.status = "Started"
        newsletter.save()
        
        if not result:
            attemptsend.status = "Successful"
        else:
            attemptsend.status = "Not_successful"
            attemptsend.news_letter.status = "Started"
        
        attemptsend.save()
        
        return super().form_valid(form)


class AttemptSendUpdate(UpdateView):
    model = AttemptSend
    form_class = Attempt_send_form
    template_name = "mailings/create.html"
    context_object_name = "attemptsend"


class AttemptSendDetail(DetailView):
    model = AttemptSend
    template_name = "mailings/detail.html"
    context_object_name = "attemptsend"


class AttemptSendView(ListView):
    model = Newsletter
    template_name = "mailings/attemptsend_list.html"
    context_object_name = "attemptsend"
