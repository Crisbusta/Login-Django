from django.urls import path, include
from auth_login import views
from django.contrib.auth import views as auth_views

app_name = 'auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    #path('profile/purchases/<int:id>', views.purchases, name='purchases'),
    path('profile/edit', views.editProfile, name='edit'),
    path('profile/change_password', views.change_password, name='change_password'),
]
