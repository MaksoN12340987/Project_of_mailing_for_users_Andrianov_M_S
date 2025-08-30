import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreateNewsletter, UpdateNewsletter, CreateMessage
from .models import Newsletter, Message

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
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        
        # for i, value in enumerate(context_data["newsletters"]):
        #     logger_views.info(value.recipients.all())
        #     context_data[value.pk] = value.recipients.all()
        # logger_views.info(context_data)
        return context_data


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
