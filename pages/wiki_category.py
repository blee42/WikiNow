# from nltk.corpus import stopwords
import urllib2, json, unicodedata
from pprint import pprint
import copy

# import nltk
# nltk.data.path.append('./nltk_data')
# from pages.nltk_data.corpora import stopwords

def get_wiki_category(titleArticle, newsArray):
	print titleArticle
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
	# stop = stopwords.words('english
	stop = open('/app/pages/nltk_data/corpora/stopwords/english','rb')
	stop_list = stop.read()
	stop.close()
	for i in titleBag.split():
		if i not in stop_list:
			if i not in ntitleBag:
				ntitleBag.append(i)

	# get list of wikipedia categories for this title
	wikiCats = get_category(titleArticle)
	wikiCount = []

	# compare news titles and categories
	nwikiCats = []
	for category in wikiCats:
		count = 0
		ncategory = copy.deepcopy(category)
		catArray = ncategory.split(" ")
		for i in catArray:
			if i in ntitleBag:
				count = count + 1
				nwikiCats.append(category)

		if count != 0:
			wikiCount.append(count)

	if len(wikiCount) == 0:
		return 'No relevant category found'
	else:
		maxCount = 0
		for count in wikiCount:
			if count > maxCount:
				maxCount = count
		index = wikiCount.index(maxCount)
		return nwikiCats[index]


def get_category(title):
	cList = []
	#title = unicode(title)
	#title = title.encode("ascii",'ignore')
	#sub_title = title.replace(' ', '%20')
	url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&prop=categories&titles=' + urllib2.quote(title)
	#url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&prop=categories&titles=' + title
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

	return cList

def get_more_categories(cList, json_result, url):
	keys = json_result.keys()
	kcontinue = 'query-continue'
	if kcontinue in keys:
		continueURL = json_result['query-continue']['categories']['clcontinue']
		nurl = url + '&clcontinue=' + continueURL
		result = urllib2.urlopen(nurl)
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




