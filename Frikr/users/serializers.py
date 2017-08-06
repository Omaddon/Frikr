# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()    # read only
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos de validated_data, que contiene valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos del diccionario validated_data que contiene
        valores deserializados.
        :param instance: modelo instanciado que vamos a actualizar
        :param validated_data: diccionario con datos del usuario para actualizar
        :return: objeto User
        """

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')

        instance.set_password(validated_data.get('password'))

        instance.save()

        return instance

    def validate_username(self, data):
        """
        Valida si existe un usuario con ese username
        """

        users = User.objects.filter(username=data)

        # Si creamos un usuario nuevo, comprobar si hay usuarios con ese username
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username.")
        # Si actualizamos un usuario (el username != instance username), comprobar si existe ese nuevo username
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username.")
        else:
            return data
