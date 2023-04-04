from django.shortcuts import render
#from django.views.generic import Listview
from miBlog.models import Alumno, Profesor, Materia
from miBlog.forms import  AlumnoForm, ProfesorForm, MateriaForm

def index(request):
    return render(request,"miBlog/index.html")

def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    context = {
        "alumnos":alumnos,
        "form":AlumnoForm(),
    }
    return render(request,"miBlog/alumnos.html",context)

def registrar_alumno(request):
    f = AlumnoForm(request.POST)
    context = {
        "form":f,
    }
    if f.is_valid:
        Alumno(nombre=f.data["nombre"],apellido=f.data["apellido"],legajo=f.data["legajo"],comienzo=f.data["comienzo"]).save()
        context["form"] = AlumnoForm()
    
    context["alumnos"] = Alumno.objects.all()
    return render(request,"miBlog/alumnos.html",context)

def mostrar_profesor(request):
    profesores = Profesor.objects.all()
    context = {
        "profesores":profesores,
        "form":ProfesorForm(),
    }
    return render(request,"miBlog/profesores.html",context)

def registrar_profesor(request):
    f = ProfesorForm(request.POST)
    context = {
        "form":f,
    }
    if f.is_valid:
        Profesor(nombre=f.data["nombre"],apellido=f.data["apellido"],catedra=f.data["catedra"]).save()
        context["form"] = ProfesorForm()

    context["profesores"] = Profesor.objects.all()
    return render(request,"miBlog/profesores.html",context)
# Create your views here.
