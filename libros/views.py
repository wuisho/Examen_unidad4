from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import LibroAddForm, LibrosModelForm
from .models import Libros


from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from biblioteca.multiSlugs import claseslug

from django.db.models import Q
from django.shortcuts import render_to_response


def home(request):

    context=locals()
    template='home.html'
    return render(request,template,context)

#Clase para agegar Libros
class AgregarNuevoLibro(CreateView):

    model = Libros

    form_class = LibrosModelForm
    success_url = "/libros/crear/"

    def get_context_data(self, *args, **kwargs):
        context = super(AgregarNuevoLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Guardar"
        return context

#Clase para lista de Libros
class ListaLibros(ListView):

    model = Libros

    def get_queryset(self, *args, **kwargs):
        qs = super(ListaLibros, self).get_queryset(**kwargs)
        return qs

#Clase para actualizar libros
class ActualizarLibro(UpdateView):
    model = Libros

    form_class = LibrosModelForm
    success_url = "/libros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Editar"
        return context

#Detalle de Libros
class DetalledeLibro(DetailView,claseslug):
    model = Libros


def lista_libros(request):
    lib = Libros.objects.all()
    print request
    mens = "Libros Registrados Actualmente"
    template = "listaDeLibros.html"
    contexto= {"Mensaje": mens,
               "Libros": lib }
    return render(request, template, contexto)

def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(Libros, id=object_id)
    form = LibrosModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libros": Libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)


def detalle_libro(request, object_id=None):

    lib = get_object_or_404(Libros, id=object_id)
    mens = "Libros Registrados Actualmente"
    template = "detalle_libro.html"
    contexto= {"Mensaje":mens,
           "Libros": lib }
    return render(request, template, contexto)


def agregar_libro(request):
    form = LibroAddForm(request.POST or None)
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        data = form.cleaned_data
        nombre = data.get("nombre")
        autor = data.get("autor")
        editorial= data.get("editorial")
        isbn= data.get("isbn")
        precio= data.get("precio")

        nuevo_libro = Libros()
        nuevo_libro.Nombre = nombre
        nuevo_libro.Autor = autor
        nuevo_libro.Editorial = editorial
        nuevo_libro.ISBN = isbn
        nuevo_libro.Precio = precio
        nuevo_libro.save()

    template = "agregar_libro.html"

    context = {
        "form":form
    }

    return render(request, template, context)
