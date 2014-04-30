import urllib2, re, json
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html')
html = response.read()

soup = BeautifulSoup(html)
# print soup2
soup3 = soup.find_all('h3')
soup3_5 = soup.find_all('div', {'class': 'summary'})
# print soup3_5

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

	# find Wikipedia image url for each article

	# ISSUE: pulls the first image in list and sometimes that is or representative of the article
	# Ex. image is of a Wikimedia logo
	# ISSUE: when the article has no images
	
	find_image = 'http://en.wikipedia.org/w/api.php?&format=json&action=query&titles=' + urllib2.quote(title[0]) + '&prop=images'
	result = urllib2.urlopen(find_image)
	json_data = json.loads(result.read())
	data = json_data[u'query'][u'pages']
	pageid = data.keys()[0]
	image_data = data[pageid][u'images'][0]
	# print
	# print image_data
	# print
	image_title = image_data[u'title']

	find_url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles=' + urllib2.quote(image_title) + '&prop=imageinfo&iiprop=url'
	result = urllib2.urlopen(find_url)
	json_data = json.loads(result.read())
	data = json_data[u'query'][u'pages']
	imageid = data.keys()[0]
	image_url = data[imageid][u'imageinfo'][0][u'url']
	print image_url
	
	print 'rank: ' + str(count)
	print 'title: ' + title[0]
	print 'url: ' + link
	print 'image url: ' + image_url
	print 'view increase: ' + stat[0]
	print 'summary: ' + summary_content[0]
	print
	count = count + 1




