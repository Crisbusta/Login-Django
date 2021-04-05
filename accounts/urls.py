from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home')
]