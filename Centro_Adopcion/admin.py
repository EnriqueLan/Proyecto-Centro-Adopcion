from django.contrib import admin
from .models import Dogs, Cats, Adopted_Pet, Avatar

@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Race', 'Gender', 'Age')
    search_fields = ('Name', 'Race', 'Gender', 'Age')
    list_filter = ('Race', 'Gender')

@admin.register(Cats)
class CatsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Race', 'Gender', 'Age')
    search_fields = ('Name', 'Race', 'Gender', 'Age')
    list_filter = ('Race', 'Gender')

@admin.register(Adopted_Pet)
class Adopted_PetAdmin(admin.ModelAdmin):
    list_display = ('User_Name', 'User_Lastname', 'User_Adress', 'Celphone_Number', 'Pet_Name', 'Pet_Race')
    search_fields = ('User_Name', 'User_Lastname', 'Pet_Name', 'Pet_Race')
    list_filter = ('Pet_Race',)

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')
    search_fields = ('user',)
