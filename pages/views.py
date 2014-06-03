from django.shortcuts import render
from .models import Page
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import grab_articles, alchemy_category, news_links

def extract_title(whole_title):
	if "..." in whole_title:
		sub_title = whole_title.split("...")
	elif "-" in whole_title:
		sub_title = whole_title.split("-")
	title = sub_title[0].rstrip()
	return title

def pages(request):
	return render(request, "index.html", locals())

def home(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-today.html'
	url_most_visited = 'http://tools.wmflabs.org/wikitrends/english-most-visited-this-week.html'
	url_downtrends = 'http://tools.wmflabs.org/wikitrends/english-downtrends-this-week.html'
	result = grab_articles.get_articles(url, "true")
	
	# does not grab news articles or categories for most_visited or downtrends
	most_visited = grab_articles.get_articles(url_most_visited, "false")
	downtrends = grab_articles.get_articles(url_downtrends, "false")
	#cache.set('downtrends', downtrends, 600)
	
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles'], "true"))
		array = x['external']

		# get wiki categories
		# x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, "index.html", locals())

def weekly(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html'
	result = grab_articles.get_articles(url, "true")
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles'], "false"))
		array = x['external']
		
		# get wiki categories
		# x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))

	return render(request, "weekly.html", locals())

def daily(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-today.html'
	result = grab_articles.get_articles(url, "true")
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles'], "false"))
		array = x['external']

		# get wiki categories
		# x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, "daily.html", locals())

def monthly(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-this-month.html'
	result = grab_articles.get_articles(url, "true")
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles'], "false"))
		array = x['external']

		# get wiki categories
		# x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, "monthly.html", locals())	
	
#cache every view
weekly = cache_page(weekly, 60 * 15)
monthly = cache_page(monthly, 60 * 15)
daily = cache_page(daily, 60 * 15)
home = cache_page(home, 60 * 15)