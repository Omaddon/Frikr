# -*- coding: utf-8 -*-

from settings import *


# Aquí modificamos lo que queramos de los settings, solo para modo develop por ejemplo.
# Ejemplo:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_DEVELOP.sqlite3'),
    }
}

# Para usar estos settings_develop en lugar de los settings, cuando migremos la bd simplemente
# le indicamos que use estos settings. Es decir, escribir en consola:
# $> python manage.py migrate --settings=frikr.settings_develop
#
# Este mismo comando lo podemos meter en la script que tenemos echa de runserver:
# runserver 0:8000 --settings=frikr.settings_develop
