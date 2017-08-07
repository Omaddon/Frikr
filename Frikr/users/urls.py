# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView


# APIRouter
router = DefaultRouter(trailing_slash=False)
router.register(r'api/1.0/users/', UserViewSet, base_name='user')

urlpatterns = [
    # Users URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
