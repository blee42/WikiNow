from nltk.corpus import stopwords
import urllib2, json, unicodedata
from pprint import pprint

def get_wiki_category(titleArticle, newsArray):
	titleBag = ''
	for article in newsArray:
		title = article['external_title']

		# remove news source
		titleOnly = title.split('-')
		titleOnly.pop()
		titleOnly = " ".join(titleOnly)

		# check type
		titleOnly = make_ascii(titleOnly)
		titleBag = titleBag + titleOnly.lower()			

	# remove punctuation
	titleBag = titleBag.translate(None, ".,:;`'")

	# remove stop words
	ntitleBag = []
	stop = stopwords.words('english')
	for i in titleBag.split():
		if i not in stop:
			if i not in ntitleBag:
				ntitleBag.append(i)

	# get list of wikipedia categories for this title
	wikiCats = get_category(titleArticle)
	# # wikiCount = []
	# print wikiCats

	# # compare news titles and categories
	# for category in wikiCats:
	# 	count = 0
	# 	print category
	# 	print
	# 	for word in category:
	# 		if word in ntitleBag:
	# 			print
	# 			print "found a word"
	# 			print word
	# 			print
	# 			# count = count + 1
	# 	# if count == 0:
	# 		# wikiCats.remove(category)
	# 	# wikiCount.append(count)

	# # print ntitleBag
	# # print wikiCats
	# # print wikiCount



def get_category(title):
	cList = []
	url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&prop=categories&titles=' + urllib2.quote(title)
	result = urllib2.urlopen(url)
	json_data = json.loads(result.read())
	data = (json_data['query']['pages'])
	result.close()

	categoryList = data[data.keys()[0]]['categories']
	for category in categoryList:
		cTitle = category['title'].split(':')[1]
		cTitle = make_ascii(cTitle)
		cList.append(cTitle.lower())

	# check if there are more categories
	cList = get_more_categories(cList, json_data, url)
	print cList

	

	return cList

def get_more_categories(cList, json_result, url):
	keys = json_result.keys()
	kcontinue = 'query-continue'
	if kcontinue in keys:
		continueURL = json_result['query-continue']['categories']['clcontinue']
		nurl = url + '&clcontinue=' + continueURL
		result = urllib2.urlopen(nurl)
		print result.read()
		json_data = json.loads(result.read())
		data = (json_data['query']['pages'])

		categoryList = data[data.keys()[0]]['categories']
		for category in categoryList:
			cTitle = category['title'].split(':')[1]
			cTitle = make_ascii(cTitle)
			cList.append(cTitle.lower())

		get_more_categories(cList, json_data, url)

	return cList



def make_ascii(s):
	if isinstance(s, str):
		return s
	elif isinstance(s, unicode):
		return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')




