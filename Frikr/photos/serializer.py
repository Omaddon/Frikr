# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoListSerializer(PhotoSerializer):

    # Para que herede el modelo, le tenemos que decir que herede de PhotoSerializer.Meta
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')
