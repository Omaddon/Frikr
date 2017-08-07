# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from photos.settings import LICENSES
from photos.validators import badwords_detector

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Pública'),
    (PRIVATE, 'Privada')
)


# Create your models here.
class Photo(models.Model):

    # Todos estos tipos son creados por Python y se encarga de tratar con la db
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="", validators=[badwords_detector])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    # En Python, los métodos que comienzan con __ son privados
    # Los que comienzan y terminan con __ son métodos especiales
    # Aunque aparezca self como parámetro, no cuenta como uno. Realmente este método tiene 0 parámetros
    def __unicode__(self):
        return self.name
