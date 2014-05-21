import urllib2, re, json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def daily():
	response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-today.html')
	html = response.read()

	soup = BeautifulSoup(html)
	# print soup2
	soup3 = soup.find_all('h3')
	soup3_5 = soup.find_all('div', {'class': 'summary'})
	# print soup3_5
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
		# if no summary
		if (len(summary.contents) == 0):
			result['summary'] = ''
		else:
			summary_content = summary.contents
			result['summary'] = summary_content[0]

		#find image link
		str_title = title[0]
		str_title = unicode(str_title)
		str_title = str_title.encode("ascii",'ignore')
		link_title = urllib2.quote(str_title)
		iquery = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + link_title

		img_response = urllib2.urlopen(iquery)
		json_data = json.loads(img_response.read())
		img_data = json_data['responseData']['results'][0]
		img_url = img_data[u'url']

		result['img'] = img_url
		
		#print 'rank: ' + str(count)
		result['ranks'] = str(count)
		#print 'title: ' + title[0]
		result['titles'] = title[0]
		#print 'url: ' + link
		result['urls'] = link
		#print 'view increase: ' + stat[0]
		result['views'] = stat[0]
		#print 'summary: ' + summary_content[0]
		#if (len(summary_content) != 0):
		#	result['summary'] = summary_content[0]
		#else:
		#	result['summary'] = "Summary not available"
		#print
		count = count + 1
		content.append(result)

	# for x in content:
	# 	print x['ranks']
	# 	print x['titles']
	# 	print x['urls']
	# 	print x['img']
	# 	print x['views']
	# 	print x['summary']
	return content


