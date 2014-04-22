import urllib2, re
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html')
html = response.read()

soup = BeautifulSoup(html)
# print soup2
soup3 = soup.find_all('h3')
soup3_5 = soup.find_all('div', {'class': 'summary'})
print soup3_5

count = 1

for x in range(0, 10):
	h3 = soup3[x]
	link = h3.find('a')
	span = h3.find('span')
	title = link.contents
	link = link.get('href')
	stat = span.contents

	summary = soup3_5[x]
	summary_content = summary.contents
	
	print 'rank: ' + str(count)
	print 'title: ' + title[0]
	print 'url: ' + link
	print 'view increase: ' + stat[0]
	print 'summary: ' + summary_content[0]
	print
	count = count + 1


