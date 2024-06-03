from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
import random

def inicio(request):
    return HttpResponse('Bienvenido al inicio')

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad} años')

def template2(request,nombre,apellido,edad):
    
    archivo_abierto = open(r'C:\Users\augus\Desktop\Data Science\Python\Django\templates\template2.html', 'r')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad    
        }
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def template3(request,nombre,apellido,edad):
    
    template = loader.get_template('template3.html')
    
    fecha = datetime.now()
    

    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad    
        }
    
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

def template4(request,nombre,apellido,edad):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad    
        }
    
    return render(request,'template2.html', datos)

def probando(request): 
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    return render(request,'probando.html', {'numeros': numeros})
# Create your views here.
