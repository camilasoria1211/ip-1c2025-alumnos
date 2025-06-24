# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests

from app.layers.transport.pokeapiFake_azul import get_pokemon_azul
from app.layers.transport.pokeapiFake_rojo import get_pokemon_rojo
from app.layers.transport.pokeapiFake_verde import get_pokemon_verde
from app.layers.transport.pokeapi_pikachu import get_pikachu
from app.layers.transport.pokeapi_charmeleon import get_charmeleon
from app.layers.transport.pokeapi_ditto import get_ditto
from app.layers.transport.pokeapi_graveler import get_graveler
from app.layers.transport.pokeapi_skiploom import get_skiploom
from app.layers.transport.pokeapi_squirtle import get_squirtle
from app.layers.transport.pokeapi_spheal import get_spheal
from ...config import config


# comunicación con la REST API.
# este método se encarga de "pegarle" a la API y traer una lista de objetos JSON.
def getAllImages():
    json_collection = []

    for _ in range(1):
        response = get_pokemon_verde()
        json_collection.append(response)
    for _ in range(1):
        response = get_pokemon_rojo()
        json_collection.append(response)
    for _ in range(1):
        response = get_pokemon_azul()
        json_collection.append(response)
    for _ in range(1):
        response = get_pikachu()
        json_collection.append(response)
    for _ in range(1):
        response = get_charmeleon()
        json_collection.append(response)
    for _ in range(1):
        response = get_ditto()
        json_collection.append(response)
    for _ in range(1):
        response = get_graveler()
        json_collection.append(response)
    for _ in range(1):
        response = get_skiploom()
        json_collection.append(response)
    for _ in range(1):
        response = get_spheal()
        json_collection.append(response)
    for _ in range(1):
        response = get_squirtle()
        json_collection.append(response)
        #funcion silenciada para no necesitar la API real de PokeAPI
       # for id in range(1, 30):
        # response = requests.get(config.STUDENTS_REST_API_URL + str(id))        
        # si la búsqueda no arroja resultados, entonces retornamos una lista vacía de elementos.    
         #if not response.ok:
          #   print(f"[transport.py]: error al obtener datos para el id {id}")
           #  continue
         #raw_data = response.json()
         #if 'detail' in raw_data and raw_data['detail'] == 'Not found.':
          #    print(f"[transport.py]: Pokémon con id {id} no encontrado.")
           #   continue
         #json_collection.append(raw_data)
        
    return json_collection

# obtiene la imagen correspodiente para un type_id especifico 
def get_type_icon_url_by_id(type_id):
    base_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/'
    return f"{base_url}{type_id}.png"