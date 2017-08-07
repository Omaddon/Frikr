# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer

# FORMA TRADICIONAL con vistas de Django en lugar de APIView
# class UserListAPI(View):
#
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         serialized_user = serializer.data               # Lista de diccionarios
#
#         renderer = JSONRenderer()
#         json_user = renderer.render(serialized_user)    # Lista de diccionarios -> JSON
#
#         return HttpResponse(json_user)


# Al usar la APIView de REST, no necesitamos indicar si es JSON, XML o lo que sea.
# Se encarga él de devolver lo que corresponda. Además de proporcionar una vista de presentación.
class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data               # Lista de diccionarios

        return Response(serialized_user)

    def post(self, request):
        # OJO!! Con REST, te guardará los datos en 'data', en lugar de POST, etc.
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        # Django nos proporciona este método común que nos devuelve el objeto de clase User con filtro pk=pk.
        # Si no lo encuentra, lanza una excepción 404-Not Found que captura el propio Django.
        user = get_object_or_404(User, pk=pk)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)