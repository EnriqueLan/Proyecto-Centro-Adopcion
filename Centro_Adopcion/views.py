from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib import messages
# Create your views here.

def home(req):
    return render(req, 'home.html')

class DogsList(ListView):

  model = Dogs
  template_name = 'perros_list.html'
  context_object_name = "perros"

class CatsList(ListView):

  model = Cats
  template_name = 'gatos_list.html'
  context_object_name = "gatos"

class DogsDetail(DetailView):

  model = Dogs
  template_name = 'perro_detail.html'
  context_object_name = "perro"

class CatsDetail(DetailView):

  model = Cats
  template_name = 'gato_detail.html'
  context_object_name = "gato"

class DogCreate(CreateView):

  model = Dogs
  template_name = 'perro_create.html'
  fields = '__all__'
  success_url = "/Centro-Adopcion/"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido creado exitosamente.')
        return response

class CatCreate(CreateView):

  model = Cats
  template_name = 'gato_create.html'
  fields = '__all__'
  success_url = "/Centro-Adopcion/"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido creado exitosamente.')
        return response


class DogDelete(DeleteView):

  model = Dogs
  template_name = 'perro_delete.html'
  success_url = "/Centro-Adopcion/"
  context_object_name = "perro"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido eliminado exitosamente.')
        return response

class CatDelete(DeleteView):

  model = Cats
  template_name = 'gato_delete.html'
  success_url = "/Centro-Adopcion/"
  context_object_name = "gato"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido eliminado exitosamente.')
        return response

class DogUpdate(UpdateView):

  model = Dogs
  template_name = 'perro_update.html'
  fields = ('__all__')
  success_url = "/Centro-Adopcion/"
  context_object_name = "perro"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido editado exitosamente.')
        return response

class CatUpdate(UpdateView):

  model = Cats
  template_name = 'gato_update.html'
  fields = ('__all__')
  success_url = "/Centro-Adopcion/"
  context_object_name = "gato"

  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido editado exitosamente.')
        return response