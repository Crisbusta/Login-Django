from django.shortcuts import render, redirect
from django.contrib import auth, messages
from auth_login.forms import RegistrationForm, EditProfileForm
from django.db import IntegrityError
from datetime import datetime
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    template_name = 'register.html'
    #data['form'] = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            auth.logout(request)
            #auth.login(request, user)
            return redirect('auth:login') 
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, template_name, args)

def login(request):
    template_name = 'login.html'
    data = {}

    auth.logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            ## Usuario autenticado
            if user.is_active:
                #Usuario valido
                auth.login(request, user)
                return redirect('auth:profile')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Error user not active.'
                )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Usuario o Contraseña incorrectos.'
            )
    else:
        return render(request, template_name, data)

def logout(request):
    auth.logout(request)
    return redirect('accounts:home')


def profile(request):
    data = {'user': UserProfile.objects.get(user=request.user.id)}
    template_name = 'profile.html'
    return render(request, template_name, data)

def editProfile(request):
    data = {}
    template_name = 'edit_profile.html'

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('auth:profile')
    else:
        form = EditProfileForm(instance=request.user)
        data = {'form': form}
        return render(request, template_name, data) 


    return render(request, template_name, data)

def change_password(request):
    data = {}
    template_name = 'change_password.html'

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('auth:profile')
        else:
            return redirect('auth:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        data = {'form': form}
        return render(request, template_name, data) 

#def purchases(request, id):
# data = {}
# template_name = 'purchases.html'
# 
# data['compras'] = Detail.objects.filter(Numero_boleta=id)
# data['total'] = Sale.objects.get(pk=id)
#   return render(request, template_name, data)