from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dogs(models.Model):

    Name=models.CharField(max_length=40, verbose_name="Nombre:")
    Race=models.CharField(max_length=40, verbose_name="Raza:")
    Gender=models.CharField(max_length=40, verbose_name="Genero:(Macho o Hembra)")
    Age=models.CharField(max_length=40, verbose_name="Edad:(Meses o Años)") #Lo puse como texto porque la idea es que puedas poner si tiene por ejemplo 2 meses o 2 años y no tener que andar haciendo calculos ponendiendo que tiene X cantidad de meses.
    Foto = models.ImageField(upload_to='fotos_mascotas', blank=True, null=True)

    def __str__(self):
        return f'{self.Name} - {self.Race}'
    
    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'

class Cats(models.Model):

    Name=models.CharField(max_length=40, verbose_name="Nombre:")
    Race=models.CharField(max_length=40, verbose_name="Raza:")
    Gender=models.CharField(max_length=40, verbose_name="Genero:(Macho o Hembra)")
    Age=models.CharField(max_length=40, verbose_name="Edad:(Meses o Años)")
    Foto = models.ImageField(upload_to='fotos_mascotas', blank=True, null=True)
    
    def __str__(self):
        return f'{self.Name} - {self.Race}'
    
    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'

class Adopted_Pet(models.Model):

    User_Name=models.CharField(max_length=40, verbose_name="Nombre Real:")
    User_Lastname=models.CharField(max_length=40, verbose_name="Apellido:")
    User_Adress=models.CharField(max_length=100, verbose_name="Su dirección:")
    Celphone_Number=models.IntegerField(verbose_name="Numero de telefono:") #Este si lo puse como Int porque solo pondrán un numero de telefono.
    Pet_Name=models.CharField(max_length=40, verbose_name="Nombre de la mascota que quiere Adoptar:")
    Pet_Race=models.CharField(max_length=40, verbose_name="Su especie(Perro o Gato):")

    def __str__(self):
        return f'{self.User_Name} - {self.Pet_Name} - {self.Pet_Race}'
    
    class Meta:
        verbose_name = 'Adopted Pet'
        verbose_name_plural = 'Adopted Pets'



class Avatar(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

  class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'