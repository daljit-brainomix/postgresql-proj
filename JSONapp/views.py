from black import format_cell
from .forms import DogForm
from django.views.generic import (
    FormView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Dog

# Create your views here.
class JSONListView(ListView):
    model = Dog
    template_name = "dogs_list.html"


class JSONDetailView(DetailView):
    model = Dog
    template_name = "dogs_detail.html"


class JSONUpdate(UpdateView):
    model = Dog
    form_class = DogForm
    # fields = ['name', 'data']
    template_name = "dog_update.html"


class JSONDelete(DeleteView):
    model = Dog
    template_name = "dog_delete.html"
    success_url = reverse_lazy("doglist")


class ContactView(FormView):
    template_name = "contact.html"
    form_class = DogForm
    success_url = "/thanks/"


class DogCreate(CreateView):
    model = Dog
    form_class = DogForm
    template_name = "dog_create.html"
    success_url = "/thanks/"
