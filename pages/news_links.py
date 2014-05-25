import urllib2;
import re
import xml.etree.ElementTree as ET

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
	if (len(items)):
		description = items[0][4].text;
		if re.findall(r"<img src=\"(.+?)\"", description):
			img_url = "http:" + re.findall(r"<img src=\"(.+?)\"", description)[0]
		# if there are no image
		else:
			img_url = "NO IMAGE"
	else:
		img_url = "NO IMAGE"
	for x in items:
		pairs = {}
		if "..." in x[0].text:
			pairs['external_only_title'] = x[0].text.split("...")[0]
			pairs['external_only_publisher'] = x[0].text.split("...")[1]
		elif "-" in x[0].text:
			pairs['external_only_title'] = x[0].text.split("-")[0]
			pairs['external_only_publisher'] = x[0].text.split("-")[1]

		pairs['external_date'] = x[3].text
		pairs['external_title'] = x[0].text
		link = x[1].text
		linkset = link.split(r'http://')
		target_url = r'http://' + linkset[-1]
		pairs['external_link'] = target_url
		pairs['external_img'] = img_url
		result.append(pairs)
	return (result)
