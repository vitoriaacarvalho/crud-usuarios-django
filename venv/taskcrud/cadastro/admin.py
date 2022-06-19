from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Usuario)
class CadastroAdmin(admin.ModelAdmin):
    readonly_fields=('nome', 'matricula','senha') 
# Register your models here.
