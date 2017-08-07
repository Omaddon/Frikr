# -*- coding: utf-8 -*-

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.serializer import PhotoSerializer, PhotoListSerializer
from photos.models import Photo


# class PhotoListAPI(APIView):
#
#     def get(self, request):
#         photos = Photo.objects.all()
#         serializer = PhotoSerializer(photos, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)


# Clases genéricas
class PhotoListAPI(ListCreateAPIView):

    queryset = Photo.objects.all()
    #serializer_class = PhotoListSerializer

    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Tenemos que llamar a este método (que nos proporciona REST) para poder hacer POST, ya que
    # de otro modo daría error al usar el PhotoListSerializer, pues le faltarían campos. Fijarse
    # que en el PhotoListSerializer solo "mostramos/accedemos" al id, name y url.
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
