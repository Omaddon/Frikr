# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from photos.forms import PhotoForm
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
    user = request.user.pk
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

# Decorador que indica que se requiere estar logueado para poder usar el create

@login_required()
def create(request):
    """
    Muestra un formulario para crear una foto y la crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        # Creamos un modelo vacío con nuestro 'owner' para pasárselo al form (owner no aparece en el form)
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user

        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            # Guarda el objeto y nos lo devuelve
            new_photo = form.save()
            form = PhotoForm()
            success_message = 'Guardado con éxito! '
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'

    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)
