# -*- coding: utf-8 -*-

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.serializer import PhotoSerializer, PhotoListSerializer
from photos.models import Photo
from photos.views import PhotosQuerySet


# class PhotoListAPI(APIView):
#
#     def get(self, request):
#         photos = Photo.objects.all()
#         serializer = PhotoSerializer(photos, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)


# Clases genéricas
class PhotoListAPI(PhotosQuerySet, ListCreateAPIView):

    queryset = Photo.objects.all()
    #serializer_class = PhotoListSerializer

    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Tenemos que llamar a este método (que nos proporciona REST) para poder hacer POST, ya que
    # de otro modo daría error al usar el PhotoListSerializer, pues le faltarían campos. Fijarse
    # que en el PhotoListSerializer solo "mostramos/accedemos" al id, name y url.
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer

    # Con esto aplicamos la política imolementada en photos.views.get_photos_queryset, la cual
    # nos da la queryset adecuada en función del usuario registrado.
    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    # Antes de guardar, la API REST siempre llama primero a este método. Lo sobreescribimos y evitamos que
    # al crear la foto se pueda especificar el 'owner', que deberá ser el del usuario logueado
    def perform_create(self, serializer):
        # De esta forma, cada vez que vaya a guardar una nueva Photo, haremos el save sobreescribiendo
        # el campo 'owner' con el que le pasamos owner=self.request.user
        serializer.save(owner=self.request.user)


class PhotoDetailAPI(PhotosQuerySet, RetrieveUpdateDestroyAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
