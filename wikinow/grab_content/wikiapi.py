import requests
import json

title = 'pizzafffdf'

r = requests.get(r'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&format=json&titles=' + title)

data = r.json()
title = data[u'query'][u'normalized']
print title