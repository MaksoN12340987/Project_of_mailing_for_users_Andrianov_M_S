import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreateNewsletter, UpdateNewsletter
from .models import Newsletter

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
    template_name = "mailings/main.html"
    context_object_name = "newsletter"


class Detail(DetailView):
    model = Newsletter
    template_name = "mailings/main.html"
    context_object_name = "newsletter"
