# -*- coding: utf-8 -*-

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.serializer import PhotoSerializer, PhotoListSerializer
from photos.models import Photo
from photos.views import PhotosQuerySet


class PhotoViewSet(PhotosQuerySet, ModelViewSet):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto al usuario autenticado.
        """
        serializer.save(owner=self.request.user)

#
#
# LO DE ABAJO ES LO MISMO QUE ESTO DE ARRIBA PERO DIVIDIDO EN DOS CLASES
#
#

# class PhotoListAPI(APIView):
#
#     def get(self, request):
#         photos = Photo.objects.all()
#         serializer = PhotoSerializer(photos, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)


# Clases genéricas
# class PhotoListAPI(PhotosQuerySet, ListCreateAPIView):
#
#     queryset = Photo.objects.all()
#     #serializer_class = PhotoListSerializer
#
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     # Tenemos que llamar a este método (que nos proporciona REST) para poder hacer POST, ya que
#     # de otro modo daría error al usar el PhotoListSerializer, pues le faltarían campos. Fijarse
#     # que en el PhotoListSerializer solo "mostramos/accedemos" al id, name y url.
#     def get_serializer_class(self):
#         return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer
#
#     # Con esto aplicamos la política imolementada en photos.views.get_photos_queryset, la cual
#     # nos da la queryset adecuada en función del usuario registrado.
#     def get_queryset(self):
#         return self.get_photos_queryset(self.request)
#
#     # Antes de guardar, la API REST siempre llama primero a este método. Lo sobreescribimos y evitamos que
#     # al crear la foto se pueda especificar el 'owner', que deberá ser el del usuario logueado
#     def perform_create(self, serializer):
#         # De esta forma, cada vez que vaya a guardar una nueva Photo, haremos el save sobreescribiendo
#         # el campo 'owner' con el que le pasamos owner=self.request.user
#         serializer.save(owner=self.request.user)
#
#
# class PhotoDetailAPI(PhotosQuerySet, RetrieveUpdateDestroyAPIView):
#
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return self.get_photos_queryset(self.request)
