from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'sobrenosotros.html')

# Seccion de Mascotas Sin Usuario:
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

# Seccion de Mascotas Con Usuario:
@method_decorator(staff_member_required, name='dispatch')
class DogCreate(LoginRequiredMixin, CreateView):
    model = Dogs
    template_name = 'perro_create.html'
    fields = '__all__'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido creado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cats
    template_name = 'gato_create.html'
    fields = '__all__'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido creado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dogs
    template_name = 'perro_delete.html'
    success_url = reverse_lazy("home")
    context_object_name = "perro"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El perro ha sido eliminado exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cats
    template_name = 'gato_delete.html'
    success_url = reverse_lazy("home")
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
    success_url = reverse_lazy("home")
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
    success_url = reverse_lazy("home")
    context_object_name = "gato"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El gato ha sido editado exitosamente.')
        return response

# Seccion de Adopciones:
class AdoptForm(LoginRequiredMixin, CreateView):
    model = Adopted_Pet
    template_name = 'adoptar.html'
    fields = '__all__'
    success_url = reverse_lazy("home")
    login_url = reverse_lazy('Login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Su Adopcion está lista. Porfavor sea paciente un miembro del refugio se pondrá en breves en comunicacion con usted')
        return response

@method_decorator(staff_member_required, name='dispatch')
class AdoptList(LoginRequiredMixin, ListView):

  model = Adopted_Pet
  template_name = 'adopciones_list.html'
  context_object_name = "adopciones"

@method_decorator(staff_member_required, name='dispatch')
class AdoptDetail(LoginRequiredMixin, DetailView):

  model = Adopted_Pet
  template_name = 'adopcion_detail.html'
  context_object_name = "adopcion"

@method_decorator(staff_member_required, name='dispatch')
class AdoptDelete(LoginRequiredMixin, DeleteView):
    model = Adopted_Pet
    template_name = 'adopcion_delete.html'
    success_url = reverse_lazy("home")
    context_object_name = "adopcion"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'La Adopcion ha sido eliminada exitosamente.')
        return response

@method_decorator(staff_member_required, name='dispatch')
class AdoptUpdate(LoginRequiredMixin, UpdateView):
    model = Adopted_Pet
    template_name = 'adopcion_update.html'
    fields = '__all__'
    success_url = reverse_lazy("home")
    context_object_name = "adopcion"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'La adopcion fue editada exitosamente.')
        return response

# Seccion de Usuarios:
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
        miFormulario = RegistroFormulario(req.POST)
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data["username"]
            miFormulario.save()
            return render(req, "home.html", {"message": f"Usuario {usuario} creado con éxito!"})
        else:
            return render(req, "home.html", {"message": "Datos inválidos"})
    else:
        miFormulario = RegistroFormulario()
        return render(req, "registro.html", {"miFormulario": miFormulario})
  
@login_required
def editar_perfil(req):
    usuario = req.user

    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            if data["password1"]:
                usuario.set_password(data["password1"])
                usuario.save()
                update_session_auth_hash(req, usuario)  #Esto hace que cuando actualizas la contraseña no te deslogee automaticamente y te lance errores(Me dió bastantes problemas entenderlo jaja).
            else:
                usuario.save()

            return render(req, "home.html", {"message": "Datos actualizados con éxito"})
        else:
            return render(req, "editar_perfil.html", {"miFormulario": miFormulario})
    else:
        miFormulario = UserEditForm(instance=req.user)
        return render(req, "editar_perfil.html", {"miFormulario": miFormulario})


def agregar_avatar(req): #Edité la view porque me estaba tirando errores cuando quería agregarle una imagen nueva al avatar y lo solucioné con el get or create.
    if req.method == 'POST':
        avatar_instance, created = Avatar.objects.get_or_create(user=req.user)
        
        miFormulario = AvatarFormulario(req.POST, req.FILES, instance=avatar_instance)
        
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "home.html", {"message": "Avatar cargado con éxito"})
        else:
            return render(req, "home.html", {"message": "Datos inválidos"})
    else:
        # Si es una solicitud GET, mostrar el formulario vacío
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})
  

@login_required
def perfil_usuario(req):
    usuario = req.user
    try:
        avatar = usuario.avatar.imagen.url
    except:
        avatar = None

    contexto = {
        "first_name": usuario.first_name,
        "last_name": usuario.last_name,
        "email": usuario.email,
        "avatar": avatar
    }
    return render(req, 'perfil_usuario.html', contexto)