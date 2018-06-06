from sys import argv
import requests
search = argv[1]
url='https://swapi.co/api/{}'.format(search)      #need to divide url to make search process more dynamic
r = requests.get(url)
d = r.json()
for i in range(10):
    print d['results'][i]['name']
url = 'https://swapi.co/api/{}'.format(search)      #need to divide url to make search process more dynamic
r = requests.get(url)
d = r.json()
for i in d['results']:
    print i['name']
