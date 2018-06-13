from sys import argv
import requests
import unicodecsv as csv
search = argv[1]
url='https://swapi.co/api/{}'.format(search) 
cast=[]
myFile=open("swap1.csv","w")
while(url != None):     
	r = requests.get(url)
	d = r.json()
	for i in d['results']:
		cast.append((i['name'], ))

	url = d['next']
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(cast)