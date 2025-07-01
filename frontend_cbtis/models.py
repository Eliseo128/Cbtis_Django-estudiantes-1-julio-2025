from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_ingreso = models.DateField()
    genero=models.CharField(max_length=50)
    materia=models.CharField(max_length=50)
    folio = models.CharField(max_length=20)
    puntuacion_examen = models.FloatField()


