# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from photos.models import Photo


# Clase modelo para personalizar nuestro Admin
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    # Con este método le decimos qué debe mostrar en la segunda columna (ver list_display arriba)
    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name

    # Con este atributo que ponemos al método le indicamos el nombre que tendrá la columna
    owner_name.short_description = u'Photo Owner'

    # Con este atributo que ponemos al método le indicamos cómo debe ordenar dicha columna
    owner_name.admin_order_field = 'owner'

    # Config Photo Detail ("model detail" del admin de Photo)
    # Tupla de tuplas. Primer elemento el título del fieldsets y luego un diccionario de configuración
    # OJO a las comas dentro de las tuplas. Una tupla de un solo elemento DEBE llevar una coma al final
    fieldsets = (
        (None, {
            'fields': ('name',),
            'classes': ('wide',)
        }),
        ('Description & Author', {
            'fields': ('description', 'owner'),
            'classes': ('wide',)
        }),
        ('Extra', {
            'fields': ('url', 'license', 'visibility'),
            'classes': ('wide', 'collapse')
        })
    )


# Si no le decimos nada, Django nos pone uno por defecto.
# Pero nosotros queremos nuestro modelAdmin "PhotoAdmin"
admin.site.register(Photo, PhotoAdmin)
