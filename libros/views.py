from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import LibroAddForm, LibrosModelForm
from .models import Libros

# Create your views here.

def home(request):

    context=locals()
    template='home.html'
    return render(request,template,context)

class LibrosListView(ListView):
    model = Libros

    def get_queryset(self, *args, **kwargs):
        setentencia = super(LibrosListView, self).get_queryset(**kwargs)
        return sentencia

class LibrosDetailView(DetailView):
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
