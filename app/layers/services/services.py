# capa de servicio/lógica de negocio

from ..transport import transport
from ...config import config
from ..persistence import repositories
from ..utilities import translator
#from django.contrib.auth import get_user

# función que devuelve un listado de cards. Cada card representa una imagen de la API de Pokemon
def getAllImages():
    imagenes_pokemon= transport.getAllImages() #imagenes obtenidas de la API. Se encuentran en Transport.py
    card_pokemon=[]
    for pokemon in imagenes_pokemon:
        card=translator.fromRequestIntoCard(pokemon) #transformamos a card
        types_aux=[]
        for t in card.types:
            types_aux.append(get_type_icon_url_by_name(t))
        card.types_imgs=types_aux #obtenemos el icono del tipo
        card_pokemon.append(card) #se ingresan las cards al listado
    return card_pokemon


# función que filtra según el nombre del pokemon.
def filterByCharacter(name):
    filtered_cards = []
    cards= getAllImages()  # obtenemos todas las cards
    for card in cards:
        if name.lower() in card.name.lower():  # si el nombre ingresado por el usuario está contenido en el nombre de la card
        # debe verificar si el name está contenido en el nombre de la card, antes de agregarlo al listado de filtered_cards.
            filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards según su tipo.
def filterByType(type_filter):
    filtered_cards = []
    all_cards = getAllImages()  # obtenemos todas las cards
    
    for card in all_cards:
        card_types_lower = [t.lower() for t in card.types]
        if type_filter.lower() in card_types_lower:
        # debe verificar si la casa de la card coincide con la recibida por parámetro. Si es así, se añade al listado de filtered_cards.
            filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    return {'success': False, 'message': 'Funcionalidad de guardar favoritos deshabilitada por el momento.'}

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    return []

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId) # borramos un favorito por su ID

#obtenemos de TYPE_ID_MAP el id correspondiente a un tipo segun su nombre
def get_type_icon_url_by_name(type_name):
    type_id = config.TYPE_ID_MAP.get(type_name.lower())
    if not type_id:
        return None
    return transport.get_type_icon_url_by_id(type_id)