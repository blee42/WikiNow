from django.shortcuts import render
from .models import Page

def pages(request):
	pages = Page.objects.all()
	return render(request, "pages.html", locals())