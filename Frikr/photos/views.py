# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    """
    Esta función devielve el home de mi página
    """
    # Con esto realmente no cargamos toda la bd, sino que tan solo "preparamos" la query de búsqueda.
    # Solo se ejecutaría la búsqueda en el último momento, cuando la variable vaya a ser utilizada.
    # Por eso, tan solo cargamos 5 datos en lugar de toda la bd como puede parecer (.objects.all)
    # photos = Photo.objects.all().order_by('-created_at')
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }

    return render(request, 'photos/home.html', context)


def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    # Una opción de recuperación de un objeto (poco elegante)
    """
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        photo = None
    except Photo.MultipleObjects:
        photo = None
    """

    # Esta opción es más elegante y legible
    # pk=pk busca por el atributo primario de búsqueda, sea cual sea. En nuestro caso, el id "pregenerado" por Django
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None

    if photo is not  None:
        # Cargamos la plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        # 404 Not Found
        return HttpResponseNotFound('No existe la foto.')