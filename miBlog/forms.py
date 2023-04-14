from django import forms

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    legajo = forms.IntegerField()
    comienzo = forms.DateField()

class MateriaForm(forms.Form):
    tema = forms.CharField(max_length=25)
    calificacion = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    catedra = forms.CharField(max_length=25)

class BuscarProfesorForm(forms.Form):
    catedra_a_buscar = forms.CharField(max_length=25)
    