from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import ListView
#from django.views.generic import Listview
from miBlog.models import Alumno, Profesor, Materia
from miBlog.forms import  AlumnoForm, ProfesorForm, MateriaForm, BuscarProfesorForm

def index(request):
    return render(request,"miBlog/index.html")

def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos,
               "form": AlumnoForm()}
    return render(request,"miBlog/alumnos.html",context)

def registrar_alumno(request):
    f = AlumnoForm(request.POST)
    context = {
        "form":f,
    }
    if f.is_valid:
        Alumno(nombre=f.data["nombre"],apellido=f.data["apellido"],legajo=f.data["legajo"],comienzo=f.data["comienzo"]).save()
        #context["form"] = AlumnoForm()
    
    context["alumnos"] = Alumno.objects.all()
    return render(request,"miBlog/alumnos.html",context)

def mostrar_profesores(request):
    profesores = Profesor.objects.all()
    context = {"profesores":profesores,
               "form": ProfesorForm()}
   
    return render(request,"miBlog/profesores.html",context)

def registrar_profesor(request):
    f = ProfesorForm(request.POST)
    context = {
        "form":f,
    }
    if f.is_valid:
        Profesor(nombre=f.data["nombre"],apellido=f.data["apellido"],catedra=f.data["catedra"]).save()
    
    context["profesores"] = Profesor.objects.all()
    return render(request,"miBlog/profesores.html",context)

def mostrar_materias(request):
    materias = Materia.objects.all()
    context = {"materias":materias,
               "form": MateriaForm()}
   
    return render(request,"miBlog/materias.html",context)

def registrar_materia(request):
    f = MateriaForm(request.POST)
    context = {
        "form":f,
    }
    if f.is_valid:
        Materia(tema=f.data["tema"],calificacion=f.data["calificacion"]).save()
    
    context["materias"] = Materia.objects.all()
    return render(request,"miBlog/materias.html",context)
def buscar_profesor(request):
    f = BuscarProfesorForm(request.GET)
    context = {
            "form":f,
    }
    if f.is_valid():
        context["profesores"] = Profesor.objects.filter(catedra__icontains=f.data.get("catedra_a_buscar")).all()
    return render(request,"miBlog/profesor_list.html",context)
