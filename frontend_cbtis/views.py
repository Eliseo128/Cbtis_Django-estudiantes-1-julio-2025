from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        fecha_ingreso = request.POST['fecha']
        genero = request.POST['genero']
        materia = request.POST['materia']
        folio = request.POST['folio']
        puntuacion_examen = request.POST['folio2']

        datos=Alumno()
        datos.nombre = nombre
        datos.correo = correo
        datos.fecha_ingreso = fecha_ingreso
        datos.genero = genero
        datos.materia = materia
        datos.folio = folio
        datos.puntuacion_examen = puntuacion_examen
        datos.save()





       
        

        # Here you can save the data to the database or perform other actions

    return render(request, 'frontend_cbtis/index.html')


def Mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'frontend_cbtis/listar_alumnos.html', {'alumnos': alumnos}) 

