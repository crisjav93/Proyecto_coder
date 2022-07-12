from django.http import HttpResponse
from django.shortcuts import render
from .models import * #el asterisco trae todas las clases
from AppCoder.forms import *

# Create your views here.

def curso(self):
    curso = Curso(nombre='Django',comision=93123)
    curso.save()
    texto=f'Curso creado: {curso.nombre} {curso.comision}'
    return HttpResponse(texto)

def inicio(request):
    return render(request,'Appcoder/inicio.html')

def cursos(request):
    return render(request,'Appcoder/cursos.html')

def profesores(request):
    return render(request,'Appcoder/profesores.html')

def estudiantes(request):
    return render(request,'Appcoder/estudiantes.html')

def entregables(request):
    return render(request,'Appcoder/entregables.html')

# def cursoFormulario(request):
    
#     if (request.method == 'POST'):
#         nombre = request.POST.get('curso')
#         comision = request.POST.get('comision')
#         curso = Curso(nombre=nombre, comision=comision)
#         curso.save()
    
#         return render(request,'Appcoder/inicio.html')    

#     return render(request, 'Appcoder/cursoFormulario.html') #vista para formulario HTML


def cursoFormulario(request):
    
    if (request.method=='POST'):
        form= CursoForm(request.POST)
        #print(form)#el print es solo para verlo como ejemplo
        if form.is_valid():
            info = form.cleaned_data#lo traen todos los formularios con una variable limplia
            #print(info)
            nombre = info['nombre']#guardo la info en los dic
            comision = info['comision']
            curso= Curso(nombre=nombre, comision=comision)#creo el curso
            curso.save()
            return render (request, 'AppCoder/inicio.html')#vuelvo a inicio
    
    else:
        form = CursoForm()
    return render(request, 'AppCoder/cursoFormulario.html',{'formulario':form})


def profeForm(request):
    
    if (request.method=='POST'):
        form= ProfeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data#lo traen todos los formularios con una variable limplia
            nombre = info['nombre']#guardo la info en los dic
            apellido = info['apellido']
            email = info['email']
            profesion = info['profesion']

            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)#creo el profesor
            profe.save()
            return render (request, 'AppCoder/inicio.html')#vuelvo a inicio
    
    else:
        form = ProfeForm()
    return render(request, 'AppCoder/profeForm.html',{'formulario':form})




def busquedaComision(request):
    
    
    return render(request, 'Appcoder/busquedaComision.html')

def buscar(request):
    if request.GET['comision']:#pregunto si hay algo en el get de comision
        comi=request.GET['comision']#entrega el contenido de comision guardandolo en comi
        cursos = Curso.objects.filter(comision=comi) #busca en la base de cursos, donde la comision es igual a la comision del formulario, y guardalo en curso
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos})
    else:
        return render(request,'AppCoder/busquedaComision.html', {'error':'No se ingreso ninguna comision'})
