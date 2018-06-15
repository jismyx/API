import requests
import csv
from googlesearch import search
f=open("/home/fullcontact-314/Downloads/artsn1.csv")
reader=csv.reader(f)
with requests.session() as c:
	url = 'https://www.google.co.in'
	query = {'q': query}
	urllink = requests.get(url, params=query)
      
for count,row in enumerate(reader):
	query=googleSearch(row)
	for j in search(urllink.url, tld="co.in", num=1, stop=1, pause=2):
		print(j)
   