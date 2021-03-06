from django.shortcuts import render
# from .models import Page
import grab_articles, alchemy_category, news_links, wiki_category

def extract_title(whole_title):
	if "..." in whole_title:
		sub_title = whole_title.split("...")
	elif "-" in whole_title:
		sub_title = whole_title.split("-")
	title = sub_title[0].rstrip()
	return title

def home(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-today.html'
	url_most_visited = 'http://tools.wmflabs.org/wikitrends/english-most-visited-this-week.html'
	url_downtrends = 'http://tools.wmflabs.org/wikitrends/english-downtrends-this-week.html'
	result = grab_articles.get_articles(url, 'true')
	
	# does not grab news articles or categories for most_visited or downtrends
	most_visited = grab_articles.get_articles(url_most_visited, 'false')
	downtrends = grab_articles.get_articles(url_downtrends, 'false')
	
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles'], 'true'))
		array = x['external']

		# get wiki categories
		# x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		# x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, 'wikinow/index.html', locals())