from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .forms import LibroAddForm
from .models import Libros


# Create your views here.

def home(request):

    context=locals()
    template='home.html'
    return render(request,template,context)

def lista_libros(request):
    lib = Libros.objects.all()
    print request
    mens = "Libros Registrados Actualmente"
    template = "listaDeLibros.html"
    contexto= {"Mensaje": mens,
               "Libros": lib }
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
