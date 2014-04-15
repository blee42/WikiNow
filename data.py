import urllib2, json
from pprint import pprint


print "Most Recent Changes:"
print

url = "https://en.wikipedia.org/w/api.php?format=json&action=query&list=recentchanges"
try:
	result = urllib2.urlopen(url)
	json_data = json.loads(result.read())
	# print pprint(json_data)
except urllib2.URLError, e:
	handleError(e)

data = json_data[u'query'][u'recentchanges']

for row in data:
	pageid = row[u'pageid']
	nquery = "https://en.wikipedia.org/w/api.php?format=json&action=query&pageids=" + str(pageid) + "&prop=info&inprop=url"

	try:
		result = urllib2.urlopen(nquery)
		json_data = json.loads(result.read())
		# print pprint(json_data)
	except urllib2.URLError, e:
		handleError(e)

	meta_data = json_data[u'query'][u'pages'][str(pageid)]
	name = meta_data[u'title']
	url = meta_data[u'fullurl']
	print name
	print url
	print

print "Articles Near Me"
print

# uses longitude and latitude for Evanston
url = "http://en.wikipedia.org/w/api.php?format=json&action=query&list=geosearch&gsradius=10000&gscoord=42.0586|-87.6845"

try:
	result = urllib2.urlopen(url)
	json_data = json.loads(result.read())
	print pprint(json_data)
except urllib2.URLError, e:
	handleError(e)

data = json_data[u'query'][u'geosearch']

for row in data:
	pageid = row[u'pageid']
	nquery = "https://en.wikipedia.org/w/api.php?format=json&action=query&pageids=" + str(pageid) + "&prop=info&inprop=url"

	try:
		result = urllib2.urlopen(nquery)
		json_data = json.loads(result.read())
		# print pprint(json_data)
	except urllib2.URLError, e:
		handleError(e)

	meta_data = json_data[u'query'][u'pages'][str(pageid)]
	name = meta_data[u'title']
	url = meta_data[u'fullurl']
	print name
	print url
	print

