from django.conf.urls import url
from django.contrib import admin

from libros import views
from libros.views import (AgregarNuevoLibro,
                             ListaLibros,
                             ActualizarLibro,
                             DetalledeLibro)

urlpatterns = [
    url(r'^lista/$', ListaLibros.as_view(), name='lista'),
    url(r'^crear/$', AgregarNuevoLibro.as_view(), name='crear'),
    url(r'^(?P<pk>\d+)/$', DetalledeLibro.as_view(), name='detalle'),
    url(r'^(?P<pk>\d+)/editar/$', ActualizarLibro.as_view(), name='actualizar'),
    url(r'^(?P<slug>[\w-]+)/$', DetalledeLibro.as_view(), name='slug_detalledelibro_view'),
]
