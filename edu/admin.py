from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass