from django import forms

from .models import Libros

OPCIONES_TIPO = (
    ('editorial solar', "Editorial Solar"),
    ('editrial portavoz', "Editorial Portavoz"),
    ('editorial rino', "Editorial Rino"),
)

class LibroAddForm(forms.Form):
    nombre=forms.CharField(label="Cual es nombre del libro",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Introduzca el nombre del libro'}))
    autor=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    editorial=forms.ChoiceField(choices=OPCIONES_TIPO)
    isbn=forms.CharField()
    precio=forms.DecimalField()

def clean_precio(self):
     precio=self.cleaned_data.get("precio")
     if precio <=200.00:
         raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
     elif precio >=19999.99:
         raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
     else:
         return precio


class LibrosModelForm(forms.ModelForm):
    editorial = forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model = Libros
        fields =[
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "Precio",
        ]
        labels = {
            "nombre": "Cual es nombre del libro",
            "autor":"Quien es el autor del libro",
            "editorial":"Cual es la editorial del libro",
            "isbn":"Cual es el isbn del libro",
            "precio":"Cual es el precio del libro",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Introduzca el nombre'}),
            "autor": forms.Textarea(attrs={'class': 'form-control'}),
            "editorial": forms.TextInput(attrs={'class': 'form-control'}),
            "isbn":forms.TextInput(attrs={'class':'form-control'}),
            "precio":forms.NumberInput(attrs={'class':'form-control'}),
        }

    def clean_precio(self):
         precio=self.cleaned_data.get("precio")
         if precio <=200.00:
             raise forms.ValidationError("El precio debe ser mayor a la cantidad de 200")
         elif precio >=19999.99:
             raise forms.ValidationError("El precio sobrepasa el rango de 19999.99")
         else:
             return precio
