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

from django.conf.urls import include, url
from django.contrib import admin

from users import urls as users_urls, api_urls as users_api_urls
from photos import urls as photos_urls, api_urls as photos_api_urls

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Users
    url(r'', include(users_urls)),
    url(r'^api/', include(users_api_urls)),

    # Photos
    url(r'', include(photos_urls)),
    url(r'^api/', include(photos_api_urls)),
]

# TODAS LAS urls JUNTAS, ANTES DE REFACTORIZAR Y SEPARARLAS POR MÓDULOS (photos/urls y photos/api_urls, users/..)
# APIRouter
# router = DefaultRouter(trailing_slash=False)
# router.register(r'api/1.0/photos', PhotoViewSet)
# router.register(r'api/1.0/users/', UserViewSet, base_name='user')
#
#
# # Con la 'r' le indicamos que es un regexp: ^ principio de cadena, $ fin de cadena
# # (?P<pk>) le decimos que capture ese dato y lo guarde en una variable llamada pk (primary key)
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     # Photos URLs
#     url(r'^$', HomeView.as_view(), name='photos_home'),
#     url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
#     url(r'^my-photos/$', login_required(UserPhotosView.as_view()),name='user_photos'),
#     url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
#     url(r'^photos/new$', CreateView.as_view(), name='create_photo'),
#
#     # API URLs
#     # SIN ROUTER
#     # url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='photo_list_api'),
#     # url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='photo_detail_api'),
#     # CON ROUTER
#     url(r'', include(router.urls)),
#
#     # Users URLs
#     url(r'^login$', LoginView.as_view(), name='users_login'),
#     url(r'^logout$', LogoutView.as_view(), name='users_logout'),
#
#     # Las APIUrls de user están ya incluídas en la línea de arriba, donde incluímos el router con las urls registradas
#     # Users API URLs
#     # url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
#     # url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
# ]
