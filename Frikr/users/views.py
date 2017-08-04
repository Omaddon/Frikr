# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.views.generic import View


# Create your views here.
from users.forms import LoginForm


class LoginView(View):

    def get(self, request):

        error_messages = []
        form = LoginForm()

        context = {
            'errors': error_messages,
            'login_form': form
        }

        # El "login_artesanal" no lo usamos. Es el primero que creamos "a mano", sin usar django.forms
        # Lo guardo aquí en lugar de git para poder comparar más fácilmente
        return render(request, 'users/login.html', context)

    def post(self, request):

        error_messages = []

        # Para usar el django.form
        form = LoginForm(request.POST)

        if form.is_valid():
            #
            # NO acceder NUNCA a los diccionarios en Python de esta forma, usar mejor su método get
            # El segundo parámetro del get es el valor por defecto si no encuentra nada
            # username = request.POST['usr']
            # username = request.POST.get('usr')
            # password = request.POST.get('pwd')

            # En lugar de trabajar directamente con el request, extraemos los datos del formulario "depurado"
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos.')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'photos_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo.')

        context = {
            'errors': error_messages,
            'login_form': form
        }

        # El "login_artesanal" no lo usamos. Es el primero que creamos "a mano", sin usar django.forms
        # Lo guardo aquí en lugar de git para poder comparar más fácilmente
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('photos_home')
