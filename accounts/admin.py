from django.contrib import admin
from accounts.models import Tabla_test, UserProfile
#admin.site.site_header= 'Admin XD'

# Register your models here.
@admin.register(Tabla_test)
class Tabla_testAdmin(admin.ModelAdmin):
    list_display = ['user', 'columna_uno']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'gender', 'city', 'phone']