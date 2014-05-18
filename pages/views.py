from django.shortcuts import render
from .models import Page
import grab_top25, grab_current, risingweekly, risingdaily, risingmonthly, test1
#import sys.path.append('../wikinow/grab_content/grab_current.py')

def pages(request):
	return render(request, "index.html", locals())

def test(request):
	headline, previous, summary, content = grab_top25.grab_25()
	#for x in content:
	#	x['external'] = (grab_top25.getLinks(x['titles']))
	return render(request, "test.html", locals())

def current(request):
	outcome = grab_current.current()
	return render(request, "test_current.html", locals())

def week(request):
	result = risingweekly.week()
	for x in result:
		titles_content = ''
		x['external'] = (grab_top25.getLinks(x['titles']))
		#print x['external']
		array = x['external']
		for y in array:
			if "..." in y['external_title']:
				sub_title = y['external_title'].split("...")
			elif "-" in y['external_title']:
				sub_title = y['external_title'].split("-")
			titles_content = titles_content + sub_title[0].rstrip() + '. '
		print titles_content
		x['category'] = (test1.getCategory(titles_content))
	return render(request, "week.html", locals())

def daily(request):
	result = risingdaily.daily()
	for x in result:
		titles_content = ''
		x['external'] = (grab_top25.getLinks(x['titles']))
		array = x['external']
		for y in array:
			if "..." in y['external_title']:
				sub_title = y['external_title'].split("...")
			elif "-" in y['external_title']:
				sub_title = y['external_title'].split("-")
			titles_content = titles_content + sub_title[0].rstrip() + '. '
		print x['titles'], titles_content
		x['category'] = (test1.getCategory(titles_content))
	return render(request, "daily.html", locals())

def monthly(request):
	result = risingmonthly.month()
	for x in result:
		titles_content = ''
		x['external'] = (grab_top25.getLinks(x['titles']))
		array = x['external']
		for y in array:
			if "..." in y['external_title']:
				sub_title = y['external_title'].split("...")
			elif "-" in y['external_title']:
				sub_title = y['external_title'].split("-")
			titles_content = titles_content + sub_title[0].rstrip() + '. '
		print titles_content
		x['category'] = (test1.getCategory(titles_content))
	return render(request, "monthly.html", locals())	