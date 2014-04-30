from django.shortcuts import render
from .models import Page
import grab_top25, grab_current, risingweekly, risingdaily
#import sys.path.append('../wikinow/grab_content/grab_current.py')

def pages(request):
	#pages = Page.objects.all()
	name = "hello world!"
	return render(request, "pages.html", locals())

def test(request):
	name = "hello world!"
	headline, previous, summary, content = grab_top25.grab_25()
	return render(request, "test.html", locals())

def current(request):
	outcome = grab_current.current()
	return render(request, "test_current.html", locals())

def week(request):
	result = risingweekly.week()
	return render(request, "week.html", locals())

def daily(request):
	result = risingdaily.daily()
	return render(request, "daily.html", locals())