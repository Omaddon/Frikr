# -*- coding: utf-8 -*-

"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from photos import views as photo_views
from users import views as user_views

# Con la 'r' le indicamos que es un regexp: ^ principio de cadena, $ fin de cadena
# (?P<pk>) le decimos que capture ese dato y lo guarde en una variable llamada pk (primary key)
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Photos URLs
    url(r'^$', photo_views.home, name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', photo_views.detail, name='photo_detail'),

    # Users URLs
    url(r'^login$', user_views.login, name='users_login'),
    url(r'^logout$', user_views.logout, name='users_logout')
]
