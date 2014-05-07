import urllib2;
from bs4 import BeautifulSoup
def grab_25():
	# https://en.wikipedia.org/wiki/Wikipedia:Top25Report
	response = urllib2.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Top25Report');
	#response = urllib2.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report/March_30_to_April_5,_2014');
	#response = urllib2.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report/March_23_to_30,_2014');
	#response = urllib2.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report/March_23_to_30,_2014');
	html = response.read();
	soup = BeautifulSoup(html);
	#print(soup.prettify());

	# headline
	title_array = soup.find_all('span', 'mw-headline');
	headline = title_array[0].text;
	#print headline;

	# summary
	p_array = soup.find_all('p');
	summary = p_array[1].get_text();
	#print summary;

	#previous link
	previous = p_array[0].a.get('href');
	previous = "https://en.wikipedia.org" + previous;
	#print previous;

	# table
	content = [];

	table_array = soup.find_all('table', 'wikitable');
	table = table_array[0];
	#print table;

	tr_array = table.find_all('tr');
	#print tr_array[10];

	#for child in tr_array[1].children:
	#	print "here";
	#	print child;

	#current_children = tr_array[10].contents;
	#print current_children[7];
	#print current_children[7].a.string;
	#print current_children[7].i.string;

	for i in range(1, 26):
		result = {};
		result['ranks'] = i;
		#print tr_array[i];
		# store views:
		current_view = tr_array[i].find_all('td', align="right");
		result['views'] = current_view[0].string;

		# store title:
		if tr_array[i].contents[7].a.string:
			#print i, "     ", tr_array[i].contents[7].a.string;
			current_title = tr_array[i].contents[7].a.string;
			#result['external'] = getLinks(tr_array[i].contents[7].a.string);
		else:
			#print i, "     ", tr_array[i].contents[7].i.string;
			current_title = tr_array[i].contents[7].i.string;
			#result['external'] = getLinks(tr_array[i].contents[7].a.string);
		
		result['titles'] = current_title
		# store links:
		current_link = "https://en.wikipedia.org" + tr_array[i].contents[7].a.get('href');
		result['links'] = current_link;
		#print current_link;

		#find image link
		img_response = urllib2.urlopen(current_link)
		html = img_response.read()
		img_soup = BeautifulSoup(html)
		img_soup2 = img_soup.find('table', {'class': 'infobox'})
		if (img_soup2):
			img_soup3 = img_soup2.find_all('img')
			if (len(img_soup3) != 0):
				img_link = img_soup3[0].get('src')
				result['img'] = 'http://' + img_link[2:]
			else:
				# print "No image in info box"
				result['img'] = "No image available"
		else:
			# print "No info box"
			img_link = img_soup.find_all('img')[0].get('src')
			result['img'] = 'http://' + img_link[2:]


		# store notes:
		#print tr_array[i].contents[-2];
		#tr_array[i].contents[-2]

		# add full link to the href in note:
		for current_a in tr_array[i].contents[-2].find_all('a'):
			tag = current_a;
			tag['href'] = "https://en.wikipedia.org" + current_a.get('href');
			#print tag['href'];

		#print tr_array[i].contents[-2];
		result['notes'] = tr_array[i].contents[-2].get_text();

		# add external links
		result['external'] = (getLinks(current_title))
		
		content.append(result);
	return (headline, previous, summary, content)

def getLinks(str):
	url = 'https://news.google.com/news/feeds?q=' + str + '&num=3&output=rss'
	# turn space into '%20', only turn it in here, cannot turn it before this function and pass through parameter
	url = url.replace(' ', '%20')
	#print url
	#rul = 'https://news.google.com/news/feeds?q=Snoop%20Dogg&num=3&output=rss'
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	#print(soup.prettify())
	items = soup.find_all('item')
	result = [];
	for x in items:
		pairs = {}
		# find titles
		titles_array = x.find_all('title')
		pairs['external_title'] = titles_array[0].string
		#titles.append(titles_array[0].string)
		#print titles_array[0].string

		# find links
		links_array = x.find_all('link')
		pairs['external_link'] = links_array[0].string
		#links.append(links_array[0].string)
		#print links_array[0].string
		result.append(pairs)
	#print result
	return (result)
