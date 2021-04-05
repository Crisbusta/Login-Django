from django.shortcuts import render, redirect
from django.contrib import auth, messages
from auth_login.forms import EditProfileForm, UserForm
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    data = {}
    template_name = 'register.html'
    data['form'] = UserForm(request.POST or None)

    if request.method == 'POST':
        if data['form'].is_valid():
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    is_active=True,
                )
                user.save()
                print('usuario registrado')

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Usuario creado con exito'
                )
                auth.login(request, user)
                return redirect('accounts:home')

                #client = Client.objects.create(
                #    age=request.POST['age'],
                #    address=request.POST['address'],
                #    rut=request.POST['rut'],
                #    phone=request.POST['phone'],
                #    user=user,
                #)

                #client.save()

            except IntegrityError as ie:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Problemas al crear el usuario ERROR: {error}.'.format(
                        error=str(ie))
                )
            #except ValidationError as ve:
            #    messages.add_message(
            #        request,
            #        messages.ERROR,
            #        'Problemas con la validación del formulario: {error}.' .format(
            #            error=str(ve))
            #    )
            
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Problemas al crear usuario',
            )

    return render(request, template_name, data)

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

    return render(request, template_name, data)

def logout(request):
    auth.logout(request)
    return redirect('accounts:home')


def profile(request):
    data = {'user': request.user}
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

def purchases(request, id):
    data = {}
    template_name = 'purchases.html'
    
    data['compras'] = Detail.objects.filter(Numero_boleta=id)
    data['total'] = Sale.objects.get(pk=id)

    return render(request, template_name, data)