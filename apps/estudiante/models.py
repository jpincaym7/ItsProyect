from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    pais = models.CharField(max_length=100)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, related_name='estudiantes')

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='asignaturas')



class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    asignaturas = models.ManyToManyField(Asignatura, related_name='profesores')
    
    


