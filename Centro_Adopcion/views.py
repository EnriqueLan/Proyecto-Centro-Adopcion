from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
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

@method_decorator(staff_member_required, name='dispatch')
class DogCreate(LoginRequiredMixin, CreateView):
    model = Dogs
    template_name = 'perro_create.html'
    fields = '__all__'
    success_url = reverse_lazy("centro_adopcion")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido creado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cats
    template_name = 'gato_create.html'
    fields = '__all__'
    success_url = reverse_lazy("centro_adopcion")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido creado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dogs
    template_name = 'perro_delete.html'
    success_url = reverse_lazy("centro_adopcion")
    context_object_name = "perro"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido eliminado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cats
    template_name = 'gato_delete.html'
    success_url = reverse_lazy("centro_adopcion")
    context_object_name = "gato"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido eliminado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dogs
    template_name = 'perro_update.html'
    fields = '__all__'
    success_url = reverse_lazy("centro_adopcion")
    context_object_name = "perro"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido editado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cats
    template_name = 'gato_update.html'
    fields = '__all__'
    success_url = reverse_lazy("centro_adopcion")
    context_object_name = "gato"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido editado exitosamente.')
        return response




def login_view(req):

  if req.method == 'POST':

    miFormulario = AuthenticationForm(req, data=req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario = data["username"]
      psw = data["password"]

      user = authenticate(username=usuario, password=psw)

      if user:
        login(req, user)
        return render(req, "home.html", {"message": f"Bienvenido {usuario}"})
      
      else:
        return render(req, "home.html", {"message": "Datos erroneos"})
    
    else:

      return render(req, "home.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = AuthenticationForm()

    return render(req, "login.html", {"miFormulario": miFormulario})
  

def register(req):

  if req.method == 'POST':

    miFormulario = UserCreationForm(req.POST)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario = data["username"]
      miFormulario.save()
      
      return render(req, "home.html", {"message": f"Usuario {usuario} creado con éxito!"})
    
    else:

      return render(req, "home.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = UserCreationForm()

    return render(req, "registro.html", {"miFormulario": miFormulario})
  
@login_required()
def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':

    miFormulario = UserEditForm(req.POST, instance=req.user)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password1"])

      usuario.save()

      return render(req, "home.html", {"message": "Datos actualizado con éxito"})
    
    else:

      return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
  
  else:

    miFormulario = UserEditForm(instance=req.user)

    return render(req, "editar_perfil.html", {"miFormulario": miFormulario})

def agregar_avatar(req):

  if req.method == 'POST':

    miFormulario = AvatarFormulario(req.POST, req.FILES)

    if miFormulario.is_valid():

      data = miFormulario.cleaned_data

      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save()

      return render(req, "home.html", {"message": "Avatar cargado con éxito"})
    
    else:

      return render(req, "home.html", {"message": "Datos inválidos"})
  
  else:

    miFormulario = AvatarFormulario()

    return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})