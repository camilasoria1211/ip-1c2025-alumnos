# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = services.getAllImages() #listado de cards de services.py
    favourite_list = []  # listado de cards de favoritos del usuario, si está logueado.
    if request.user.is_authenticated:
        favourite_list = services.getAllFavourites(request)  #listado de cards de favoritos del usuario, si está logueado.

    return render(request, 'home.html', { 'images': images,'favourite_list': favourite_list })

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
def search(request):
    name = request.POST.get('query', '')
    # Si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images =services.filterByCharacter(name) # debe traer un listado filtrado de imágenes, segun si es o contiene ese nombre.
        favourite_list = []
        if request.user.is_authenticated:
            favourite_list = services.getAllFavourites(request)
       
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon
def filter_by_type(request):
    type_filter = request.POST.get('type', '')

    if type_filter != '':
        images = services.filterByType(type_filter)  # debe traer un listado filtrado de imágenes, segun si es o contiene ese tipo.
        favourite_list = []
        if request.user.is_authenticated:
            favourite_list = services.getAllFavourites(request)

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    return render (request, 'proximamente_favourites.html')

@login_required
def saveFavourite(request):
    if request.method == 'POST':
        result=services.saveFavourite(request)
        return redirect('home')
    
@login_required
def deleteFavourite(request):
    return redirect('home')

@login_required
def exit(request):
    logout(request)
    return redirect('home')