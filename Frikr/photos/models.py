# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)


# Create your models here.
class Photo(models.Model):

    # Todos estos tipos son creados por Python y se encarga de tratar con la db
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)

    # En Python, los métodos que comienzan con __ son privados
    # Los que comienzan y terminan con __ son métodos especiales
    # Aunque aparezca self como parámetro, no cuenta como uno. Realmente este método tiene 0 parámetros
    def __unicode__(self):
        return self.name
