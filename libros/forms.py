from django import forms

class LibroAddForm(forms.Form):
    nombre=forms.CharField()
    autor=forms.CharField()
    editorial=forms.CharField()
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
