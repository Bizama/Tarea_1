from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

'''
def index(request):
    r = requests.get('https://rickandmortyapi.com/api/')
    r = r.json()
    context = {'personajes': r['characters'],
                'ubicacion': r['locations'],
                'episodios': r['episodes'],
                }
    return render(request, 'polls/index.html', context)
'''
def index(request):
    r = requests.get('https://rickandmortyapi.com/api/episode/')
    r = r.json()
    context = {
        'results': r['results'],
        'next_page': r['info']['next'],
        'prev_page': r['info']['prev'],
        'words': ['name', 'air_date', 'episode'],
                }
    return render(request, 'polls/index.html', context)

def index_2(request):
    r = requests.get('https://rickandmortyapi.com/api/episode?page=2')
    r = r.json()
    context = {
        'results': r['results'],
        'next_page': r['info']['next'],
        'prev_page': r['info']['prev'],
        'words': ['name', 'air_date', 'episode'],
                }
    return render(request, 'polls/2.html', context)


def characters(request, id):
    url = 'https://rickandmortyapi.com/api/character/{}'.format(id)
    r = requests.get(url)
    r = r.json()
    origin = r['origin']['name']
    origin_url = r['origin']['url'][-1]
    location = r['location']['name']
    location_url = r['location']['url'][-1]
    lista_epis = r['episode']
    episodios = list()
    for i in lista_epis:
        res = requests.get(i)
        res = res.json()
        nombre = res['name']
        episodios.append(nombre)

    context = {
        'name': r['name'],
        'status': r['status'],
        'species': r['species'],
        'type': r['type'],
        'gender': r['gender'],
        'origin': origin,
        'location': location,
        'episode': episodios,
        'id_location': location_url,
        'id_origin': origin_url
    }

    return render(request, 'polls/characters.html', context)


def locations(request, id):
    url = 'https://rickandmortyapi.com/api/location/{}'.format(id)
    data = requests.get(url)
    data = data.json()
    names = data['residents']
    neims = list()
    for i in names:
        url_pers = i
        pers_name_a = requests.get(url_pers)
        pers_name_a = pers_name_a.json()
        n = pers_name_a['name']
        neims.append(n)
    context = {
            'name': data['name'],
            'type': data['type'],
            'dimension': data['dimension'],
            'residents': neims,
                }

    return render(request, 'polls/locations.html', context)


def episodes(request, id):
    url = 'https://rickandmortyapi.com/api/episode/{}'.format(id)
    r = requests.get(url)
    r = r.json()
    nombres = []
    phone_book = dict()
    personajes = r['characters']

    for i in personajes:
        url_pers = i
        pers_name = requests.get(url_pers)
        pers_name = pers_name.json()
        n = pers_name['name']
        id = pers_name['id']
        nombres.append(id)
        phone_book[id] = n

    context = {
        'name': r['name'],
        'air_date': r['air_date'],
        'characters': nombres,
        'episode': r['episode'],
        'phone_book': phone_book
    }
    return render(request, 'polls/episodes.html', context)
