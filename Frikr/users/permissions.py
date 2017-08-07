# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario atutenticado en request.user tiene permiso
        para realizar la acción (GET, POST, PUT o DELETE)
        """
        # OJO!!!! Hay que importar localmente en tiempo de ejecucción para evitar dependencias cíclicas
        from users.api import UserDetailAPI

        if request.method == 'POST':
            # Todos pueden crear un usuario
            return True
        elif request.user.is_superuser:
            # Si el user es admin, puede hacer lo que quiera
            return True
        # Llegados aquí, el user no es admin y la petición NO es Post
        # Si la petición es Get, Put o Delete sobre la vista de detalle, se podrá hacer y
        # se evaluará en has_object_permission. Pero si es sobre una lista, NO se podrá
        elif isinstance(view, UserDetailAPI):
            return True
        else:
            # GET a /api/1.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene permiso
        para realizar la acción (GET, PUT o DELETE) sobre el object obj
        """

        return request.user.is_superuser or request.user == obj
