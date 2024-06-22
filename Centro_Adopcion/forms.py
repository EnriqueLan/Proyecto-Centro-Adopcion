from django import forms
from .models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class RegistroFormulario(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model=User
    fields=["email", "first_name", "last_name",]
    labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }


class AvatarFormulario(forms.ModelForm):

  class Meta:
    model=Avatar
    fields=('imagen',)