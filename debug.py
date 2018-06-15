# coding: utf-8
from google_scraper import google_search
import csv
f = open("/home/fullcontact-314/Downloads/artsn1.csv")
reader = csv.reader(f)
search_terms = [ x[0] for x in reader ]
res = google_search(search_terms[0])