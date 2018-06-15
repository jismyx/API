# coding: utf-8
import requests
r = requests.get("https://www.google.com/search?q=amonguzz%40cisco.com%2BLinkedin")
r.status_code
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
soup.find_all("div", {"class":"g"})
soup.find_all("div", {"class":"g"})[0]
soup.find_all("div", {"class":"g"})[1]
soup.find_all("div", {"class":"g"})[2]
soup.find_all("div", {"class":"g"})[0]
