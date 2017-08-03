# -*- coding: utf-8 -*-

from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

# Busca un LICENSES en settings. Si no lo encuentra, usará las Default aquí definidas
LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)


BADWORDS = getattr(settings, 'PROJECT_BADWORDS', [])