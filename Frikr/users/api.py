# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.renderers import JSONRenderer

from users.serializers import UserSerializer


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        serialized_user = serializer.data               # Lista de diccionarios
        renderer = JSONRenderer()
        json_user = renderer.render(serialized_user)    # Lista de diccionarios -> JSON

        return HttpResponse(json_user)
