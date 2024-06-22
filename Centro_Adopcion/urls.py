from django.urls import path
from Centro_Adopcion.views import *
from Centro_Adopcion import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('', views.home, name='home'),
   path('lista-perros', DogsList.as_view(), name='perros_list'),
   path('lista-gatos', CatsList.as_view(), name='gatos_list'),
   path('detalle-perro/<pk>', DogsDetail.as_view(), name='DetallePerro'),
   path('detalle-gato/<pk>', CatsDetail.as_view(), name='DetalleGato'),
   path('crea-perro/', DogCreate.as_view(), name='CreaPerro'),
   path('crea-gato/', CatCreate.as_view(), name='CreaGato'),
   path('elimina-perro/<pk>', DogDelete.as_view(), name='EliminaPerro'),
   path('elimina-gato/<pk>', CatDelete.as_view(), name='EliminaGato'),
   path('actualiza-perro/<pk>', DogUpdate.as_view(), name='ActualizaPerro'),
   path('actualiza-gato/<pk>', CatUpdate.as_view(), name='ActualizaGato'),
   path('login/', login_view, name='Login'),
   path('registrar/', register, name='Registrar'),
   path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
   path('about/', views.about, name='sobrenosotros'),
   path('adoptar/', AdoptForm.as_view(), name='AdoptarMascota'),
   path('lista-adopciones/', AdoptList.as_view(), name='adopciones_list'),
   path('detalle-adopcion/<pk>', AdoptDetail.as_view(), name='DetalleAdopcion'),
   path('elimina-adopcion/<pk>', AdoptDelete.as_view(), name='EliminaAdopcion'),
   path('actualiza-adopcion/<pk>', AdoptUpdate.as_view(), name='ActualizaAdopcion'),
   path('editar-perfil', editar_perfil, name='EditarPerfil'),
   path('perfil-usuario/', views.perfil_usuario, name='perfil_usuario'),
   path('agregar-avatar/', agregar_avatar, name='CreaAvatar'),
]