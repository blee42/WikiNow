from django.shortcuts import render
from .models import Page
import grab_top25, grab_current, risingweekly, risingdaily
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
		x['external'] = (grab_top25.getLinks(x['titles']))
	return render(request, "week.html", locals())

def daily(request):
	result = risingdaily.daily()
	for x in result:
		x['external'] = (grab_top25.getLinks(x['titles']))
	return render(request, "daily.html", locals())