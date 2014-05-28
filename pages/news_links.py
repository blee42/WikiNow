import urllib2, json, re, types, unicodedata
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def getimgs(news_title):
	# print news_title
	# print
	#print article_title
	news_title = unicode(news_title)
	news_title = news_title.encode("ascii",'ignore')
	news_title = urllib2.quote(news_title)
	#news_title = news_title.replace(' ', '%20')
	iquery = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + news_title
	img_response = urllib2.urlopen(iquery)
	json_data = json.loads(img_response.read())
	if (json_data['responseStatus'] == 200) and (len(json_data['responseData']['results']) > 0):
		img_data = json_data['responseData']['results'][0]
		img_url = img_data[u'unescapedUrl']
	else:
		img_url = "no img"
	# print img_url
	return img_url

# use elementtree
def getLinks(str):
	# ignore special characters
	str = unicode(str);
	str = str.encode("ascii",'ignore');
	url = 'https://news.google.com/news/feeds?q=' + urllib2.quote(str) + '&num=3&output=rss'

	# turn space into '%20', only turn it in here, cannot turn it before this function and pass through parameter
	#url = url.replace(' ', '%20')
	
	response = urllib2.urlopen(url)
	html = response.read()
	soup = ET.fromstring(html)
	items = soup[0].findall('item')
	result = []
	# if (len(items)):
	# 	description = items[0][4].text;
	# 	if re.findall(r"<img src=\"(.+?)\"", description):
	# 		img_url = "http:" + re.findall(r"<img src=\"(.+?)\"", description)[0]
	# 	# if there are no image
	# 	else:
	# 		img_url = "NO IMAGE"
	# else:
	# 	img_url = "NO IMAGE"
	for x in items:
		pairs = {}
		if "..." in x[0].text:
			pairs['external_only_title'] = x[0].text.split("...")[0]
			pairs['external_only_publisher'] = x[0].text.split("...")[1]
		elif "-" in x[0].text:
			pairs['external_only_title'] = x[0].text.split("-")[0]
			pairs['external_only_publisher'] = x[0].text.split("-")[1]

		# grab image of each news article
		article_title = pairs['external_only_title']

		title = make_ascii(article_title)
		title_normal = title.translate(None, ".,:;`'")
		img_url = getimgs(title_normal)
		
		#img_url = "no image"
		pairs['external_date'] = x[3].text
		pairs['external_title'] = x[0].text
		link = x[1].text
		linkset = link.split(r'http://')
		target_url = r'http://' + linkset[-1]
		pairs['external_link'] = target_url
		pairs['external_img'] = img_url
		result.append(pairs)
		#print pairs['external_only_title'], pairs['external_img']
	return (result)

def make_ascii(s):
	if isinstance(s, str):
		return s
	elif isinstance(s, unicode):
		return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
