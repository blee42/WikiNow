import urllib2, re
from bs4 import BeautifulSoup
import requests
import json

r = requests.get(r"http://en.wikipedia.org/wiki/User:West.andrew.g/Popular_pages")
html = r.text

soup = BeautifulSoup(html)
table = soup.find('table', {'class': 'wikitable'})

for row in table.findAll('tr')[1:]:
	col = row.findAll('td')
	entry = col[1]
	title = entry.text
	link = entry.find('a').get('href')
	print title, link