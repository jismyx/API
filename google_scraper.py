# coding: utf-8
import requests
from urllib import urlencode
from bs4 import BeautifulSoup


def google_search(search_term):
	print search_term
	parameters = {'q':search_term}
	url = "https://www.google.com/search?{}".format(urlencode(parameters))
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	item = soup.find("div", {"class":"g"})
	try:
		link = item.find("cite").text
	except AttributeError:
		link = ""
	return link