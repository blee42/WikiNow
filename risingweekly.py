import urllib2, re
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html')
html = response.read()

soup = BeautifulSoup(html)
soup2 = soup.find('div', {'id': 'topics'})
soup3 = soup2.find_all('li')

count = 1

for el in soup3:
	soup4 = el.find('h3')

	for title in soup4.find_all('a'):
		content = title.contents
		print 'rank: ' + count
		print 'title: ' + content[0]
		print 'url: ' + title.get('href')
		print
		count = count + 1

# add rank, title, link, summary, percentage increase


