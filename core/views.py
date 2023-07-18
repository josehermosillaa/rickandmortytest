import requests

from django.shortcuts import render, HttpResponse
from .models import Personaje
# Create your views here.

def home_view(request):
    personajes = Personaje.objects.all() #nos traemos todos los personajes
    context = {"personajes":personajes}
    return render(request, template_name="core/mostrar.html", context=context)

def get_rick_data_view(request):
    url = "https://rickandmortyapi.com/api/character"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # print(data["results"])  #es una lista de python , que contiene diccionarios dentro
        #name, status, species, gender
        resultado  = data["results"] #lista de diccionarios 
        for dato in resultado:  #dato va a ser cada diccionario dentro de la lista
            #[para acceder a sus datos usamos las claves]

            Personaje.objects.update_or_create(
                name=dato["name"],
                status=dato["status"],
                species=dato["species"],
                gender=dato["gender"],
                image=dato["image"]
                )
        return HttpResponse("<h1> Los datos fueron cargados correctamente </h1>")
    else:
        HttpResponse("<h1> Los datos no se pudieron cargar </h1>")