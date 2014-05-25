from django.shortcuts import render
from .models import Page
import grab_articles, alchemy_category, wiki_category, news_links

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
<<<<<<< HEAD
	result = risingdaily.daily()
=======
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html'
	result = grab_articles.get_articles(url)
>>>>>>> ba243939e811664ad353cc87070bfbc417a68409
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles']))
		array = x['external']

		# get wiki categories
		x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
<<<<<<< HEAD
			if "..." in y['external_title']:
				sub_title = y['external_title'].split("...")
			elif "-" in y['external_title']:
				sub_title = y['external_title'].split("-")
			titles_content = titles_content + sub_title[0].rstrip() + '. '
		#print x['titles'], titles_content
		x['category'] = (test1.getCategory(titles_content))
=======
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
>>>>>>> ba243939e811664ad353cc87070bfbc417a68409
	return render(request, "index.html", locals())

def weekly(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html'
	result = grab_articles.get_articles(url)
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles']))
		array = x['external']
		
		# get wiki categories
		x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))

	return render(request, "weekly.html", locals())

def daily(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-today.html'
	result = grab_articles.get_articles(url)
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles']))
		array = x['external']

		# get wiki categories
		x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, "daily.html", locals())

def monthly(request):
	url = 'http://tools.wmflabs.org/wikitrends/english-uptrends-this-month.html'
	result = grab_articles.get_articles(url)
	for x in result:
		titles_content = ''
		x['external'] = (news_links.getLinks(x['titles']))
		array = x['external']

		# get wiki categories
		x['cat'] = wiki_category.get_wiki_category(x['titles'],array)

		# get alchemy categories
		for y in array:
			title = extract_title(y['external_title'])
			titles_content = titles_content + title + '. '
		x['category'] = (alchemy_category.getCategory(titles_content))
	return render(request, "monthly.html", locals())	