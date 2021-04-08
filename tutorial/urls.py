from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('auth/', include('auth_login.urls')),
    #Me trae las funciones de reseteo de contraseña que provee Django
    path('accounts/', include('django.contrib.auth.urls')), 
]
