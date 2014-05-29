import urllib2, re, json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def get_articles(current_url):
	#response = urllib2.urlopen('http://tools.wmflabs.org/wikitrends/english-uptrends-today.html')
	response = urllib2.urlopen(current_url)
	html = response.read()

	soup = BeautifulSoup(html)
	soup3 = soup.find_all('h3')
	soup3_5 = soup.find_all('div', {'class': 'summary'})
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
		iquery = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&imgsz=xxlarge&q=' + link_title
		# iquery = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&tbs=iar:s&q=' + link_title

		try:
			# img_response = urllib2.urlopen(iquery)
			img_response = urllib2.Request(iquery, None, {'Referer': 'wikinow.herokuapp.com'})
			response = urllib2.urlopen(img_response)
			# json_data = json.loads(img_response.read())
			json_data = json.loads(response.read())

			response = json_data['responseData']
			if (response is None):
				result['img'] = 'google error'		
			else:	
				img_data = response['results'][0]
				img_url = img_data[u'url']
				result['img'] = img_url
			
		except urllib2.URLError, e:
			handleError(e)
			result['img'] = 'No image available'
		
		
		
		#print 'rank: ' + str(count)
		result['ranks'] = str(count)
		#print 'title: ' + title[0]
		result['titles'] = title[0]
		#print 'url: ' + link
		result['urls'] = link
		#print 'view increase: ' + stat[0]
		result['views'] = stat[0]
		count = count + 1
		content.append(result)
	return content


