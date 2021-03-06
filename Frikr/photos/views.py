# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.db.models import Q

# Create your views here.
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


class PhotosQuerySet(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            # Esta operación de query nos hace un AND. Queremos un OR!!
            #photos = Photo.objects.filter(owner=request.user, visibility=PUBLIC)

            # Con esto hacemos un OR de búsqueda
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))

        # Realmente no nos devuelve las fotos, sino un "query configurada" para realizar la búsqueda.
        # No se irá a buscar a la bd hasta que realmente se vayan a usar los datos.
        # Por ello, en DetailView podemos seguir configurando la query antes de lanzar la búsqueda.
        return photos


class HomeView(View):

    def get(self, request):
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


class DetailView(View, PhotosQuerySet):

    def get(self, request, pk):
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
        # pk=pk busca por el atributo primario de búsqueda, sea cual sea. En nuestro caso,
        # el id "pregenerado" por Django
        # Con 'select_related()' hacemos una especie de join de tablas de la bd para que se traiga
        # más cosas de la bd
        # Con 'prefetch_related()' hacemos lo mismo pero a la inversa. Traemos las photos relacionadas con un user
        possible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
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


class CreateView(View):

    # Decorador 'login_required' que indica que se requiere estar logueado para poder usar el create
    # Debemos decorar el decorador, pues dicho decorador solo funciona con funciones, no con métodos de clase
    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crear una foto
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        form = PhotoForm()

        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Crea una foto en base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''

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


class PhotoListView(View, PhotosQuerySet):

    def get(self, request):
        """
        Devuelve:
            - Las fotos públicas si el user no está autenticado
            - Las fotos del user logueado O las públicas de otros
            - Todas las fotos si el user logueado es admin
        :param request: HttpRequest
        :return: HttpResponse
        """

        context = {
            'photos': self.get_photos_queryset(request)
        }

        return render(request, 'photos/photos_list.html', context)


class UserPhotosView(ListView):
    # CLASE GENÉRICA
    # Tan solo le indicamos el modelo y la plantilla a renderizar
    # Por defecto, nos devuelve la lista de objetos del tipo del modelo en "object_list"
    model = Photo
    template_name = 'photos/user_photos.html'

    # Le indicamos que queremos filtrar los modelos por el usuario logueado
    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()

        return queryset.filter(owner=self.request.user)
