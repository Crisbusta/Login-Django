from django.contrib import admin
from accounts.models import Tabla_test
# Register your models here.

@admin.register(Tabla_test)
class Tabla_testAdmin(admin.ModelAdmin):
    list_display = ['user', 'columna_uno']