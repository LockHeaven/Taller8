from django.shortcuts import render, redirect
from .models import *
from .forms import PersonaForm

def home(request):
    return render(request,'index.html')


def crearUsuario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request,'crear_usuario.html',{'form':form})

def listarUsuario(request):
    persona = Persona.objects.all()
    context = {'persona':persona}
    return render(request,'listar_usuario.html',context)

def editarUsuario(request,id):
    #persona = Persona.objects.get(id=id)
    #return render(request,'editar_usuario.html',{'persona':persona})
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
    else:
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'editar_usuario.html',{'form':form})

def eliminarUsuario(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'POST':
        persona.delete()
        return redirect('index')
    return render(request,'eliminar_usuario.html',{'persona':persona})


Bucaramanga = ciudad(
    nombre = 'Bucaramanga',
    descripcion = 'Bucaraanga capital de Santander.'
)

Bucaramanga.save()

Medellin = ciudad(
    nombre = 'Medellin',
    descripcion = 'He ave maria pues home, gonorrea'
)

Medellin.save()

Cedula = tipodocumento(
    nombre = 'Cedula',
    descripcion = 'Para mayores wey'
)

Cedula.save()

Tarjeta = tipodocumento(
    nombre = 'Tarjeta de identidad',
    descripcion = 'Para menores wey'
)

Tarjeta.save()


