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
			result['titles'] = tr_array[i].contents[7].a.string;
		else:
			#print i, "     ", tr_array[i].contents[7].i.string;
			result['titles'] = tr_array[i].contents[7].i.string;
			
		# store links:
		current_link = "https://en.wikipedia.org" + tr_array[i].contents[7].a.get('href');
		result['links'] = current_link;
		#print current_link;

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
		#tr_array[i].contents[-2].href = "https://en.wikipedia.org" + 
		content.append(result);
	return (headline, previous, summary, content)
