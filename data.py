import urllib2, json
from pprint import pprint

url ="https://en.wikipedia.org/w/api.php?format=json&action=query&list=recentchanges"
try:
	result = urllib2.urlopen(url)
	json_data = json.loads(result.read())
	# print pprint(json_data)
except urllib2.URLError, e:
	handleError(e)

data = json_data[u'query'][u'recentchanges']

# for row in data:
# 	nquery = "https://en.wikipedia.org/w/api.php?action=query&pageids=" + str(row[u'pageid']) + "&prop=info&inprop=url"
# 	print nquery
# 	result = urllib2.urlopen(nquery)
# 	json_data = json.loads(result.read())
# 	print pprint(json_data)

row = data[0]
nquery = "https://en.wikipedia.org/w/api.php?format=json&action=query&pageids=" + str(row[u'pageid']) + "&prop=info&inprop=url"
print nquery
print
pageid = row[u'pageid']
print pageid
try:
	result = urllib2.urlopen(nquery)
	json_data = json.loads(result.read())
	# print pprint(json_data)
except urllib2.URLError, e:
	handleError(e)

data = json_data[u'query'][u'pages'][str(pageid)][u'fullurl']
print data
