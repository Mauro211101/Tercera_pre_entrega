from django.db import models

class Alumno(models.Model):
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    legajo = models.IntegerField()
    comienzo = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} -- {self.nombre} -- {self.legajo}"

class Materia(models.Model):
    tema = models.TextField(max_length=25)
    calificacion = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} -- {self.tema} -- {self.calificacion}"

class Profesor(models.Model):
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    catedra = models.TextField(max_length=25)

    def __str__(self) -> str:
        return f"{self.id} -- {self.nombre}, {self.apellido} -- {self.catedra}"