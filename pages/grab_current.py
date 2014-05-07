import urllib2;
from bs4 import BeautifulSoup

# https://en.wikipedia.org/wiki/Wikipedia:Top25Report
def current():

	response = urllib2.urlopen('https://en.wikipedia.org/wiki/Portal:Current_events');
	html = response.read();
	soup = BeautifulSoup(html);
	#print(soup.prettify());
	table_array = soup.find_all('table');
	#for table in table_array:
	#	print;
	#	print table;
	#print table_array[2];
	subtable = table_array[2].find_all('table', 'vevent');
	# for stable in subtable:
	# 	print;
	# 	print stable;
	#print "~~~~~~~~~~~~";
	#print subtable[0];
	target_table = subtable[1];
	target_td = target_table.find_all('td', 'description');
	#print target_td;
	target_td = target_td[0];
	#print target_td.prettify();
	#print;
	sub_dl = target_td.find_all('dl');
	dl = [];
	content = [];

	count = 0;
	for sub in sub_dl:
		topics = {};
		topics['title'] = sub.dt.string;
		dl.append(sub.dt.string);
		#print;
		#print sub.dt.string;
		sub_ul = sub.next_sibling.next_sibling;
		# sub is title
		print "sub begin!!!!!!!!"
		print sub.dt.string;
		print "sub end!!!!!!!!"
		# add integrated href
		#for current_a in sub_ul.find_all('a'):
		#	tag = current_a;
		#	tag['href'] = "https://en.wikipedia.org" + current_a.get('href');
		#print "sub_ul begin ********"
		#print sub_ul;
		#print "sub_ul end *********"
		topics['notes'] = sub_ul;
		#for ul in sub_ul:
			# ul is content
			#print "~~~~~~~~ul begin";
			#print ul;
			#print "~~~~~~~~ul end";
			#content.append(ul);
			#print ul;
		#dl[0].append(content);
		#topics[dl[count]] = content;
		#topics['notes'] = 
		content.append(topics)
		count = count + 1;

	#print topics;
	#print "~~~~~~~~";
	# for a in content:
	# 	print a['title']
	# 	print a['notes']

	return content
#print topics

# #print target_td.dl;