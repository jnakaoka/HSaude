from django.contrib import admin
from .models import Medicos

# Register your models here.
@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']   