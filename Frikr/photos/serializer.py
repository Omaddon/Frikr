# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

        # Con esto le decimos que no es necesairo que nos manden el owner, ya que lo
        # sobreescribimos con el user logueado que la está creando
        read_only_fields = ('owner',)


class PhotoListSerializer(PhotoSerializer):

    # Para que herede el modelo, le tenemos que decir que herede de PhotoSerializer.Meta
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')
