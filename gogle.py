import csv
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
f=open("/home/fullcontact-314/Downloads/artsn1.csv")
reader=csv.reader(f)
for count,row in enumerate(reader):
	query =row[0]
	for j in search(query, tld="co.in", num=1, stop=1, pause=2):
		print(j)
   