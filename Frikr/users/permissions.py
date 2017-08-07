# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario atutenticado en request.user tiene permiso
        para realizar la acción (GET, POST, PUT o DELETE)
        """
        # Todos pueden crear un usuario
        if view.action == 'create':
            return True
        # Si el user es admin, puede hacer lo que quiera
        elif request.user.is_superuser:
            return True
        # Si es un GET a la vista de detalle, se decide en has_object_permission
        elif view.action in ['retrieve', 'update', 'destroy']:
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
