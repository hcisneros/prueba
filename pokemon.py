import json
# from urllib import urlopen
import requests

#   https://pokeapi.co/api/v2/pokemon/3/
base = 'http://pokeapi.co/api/v2/pokemon/'
pokemon_list = []
for i in range(1, 152):
    url = '%s%s' % (base, i)
    response = requests.get(url)
    result = json.loads(response.content)
    types = {}
    for t in result['types']:
        types.update({t['slot']: t['type']['name']})
    pokemon = {
        'id': i,
        'name': result['name'],
        'types': types,
        'sprite': result['sprites']['front_default'],

    }
    pokemon_list.append(pokemon)
print pokemon_list
