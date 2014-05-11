import urllib2, re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def month():
	response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-this-month.html')
	html = response.read()

	soup = BeautifulSoup(html)
	# print soup2
	soup3 = soup.find_all('h3')
	soup3_5 = soup.find_all('div', {'class': 'summary'})
	#print soup3_5
	content = [];
	count = 1

	for x in range(0, 10):
		result = {};
		h3 = soup3[x]
		link = h3.find('a')
		span = h3.find('span')
		title = link.contents
		link = link.get('href')
		stat = span.contents

		summary = soup3_5[x]
		summary_content = summary.contents

		#find image link
		img_response = urllib2.urlopen(link)
		html = img_response.read()
		img_soup = BeautifulSoup(html)
		img_soup2 = img_soup.find('table', {'class': 'infobox'})
		if (img_soup2):
			img_soup3 = img_soup2.find_all('img')
			if (len(img_soup3) != 0):
				img_link = img_soup3[0].get('src')
				result['img'] = 'http://' + img_link[2:]
			else:
				# print "No image in info box"
				result['img'] = "No image available"
		else:
			# print "No info box"
			img_link = img_soup.find_all('img')[0].get('src')
			result['img'] = 'http://' + img_link[2:]
		
		#print 'rank: ' + str(count)
		result['ranks'] = str(count)
		#print 'title: ' + title[0]
		result['titles'] = title[0]
		#print 'url: ' + link
		result['urls'] = link
		#print 'view increase: ' + stat[0]
		result['views'] = stat[0]
		#print 'summary: ' + summary_content[0]
		result['summary'] = summary_content[0]
		#print
		count = count + 1
		content.append(result)

	# for x in content:
	# 	print x['ranks']
	# 	print x['titles']
	# 	print x['urls']
	# 	print x['views']
	# 	print x['summary']
	return content


