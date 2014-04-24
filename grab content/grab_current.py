import urllib2;
from bs4 import BeautifulSoup

# https://en.wikipedia.org/wiki/Wikipedia:Top25Report

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
target_table = subtable[0];
target_td = target_table.find_all('td', 'description');
#print target_td;
target_td = target_td[0];
#print target_td.prettify();
#print;
sub_dl = target_td.find_all('dl');
dl = [];
topics = {};
count = 0;
for sub in sub_dl:
	content = [];
	dl.append(sub.dt.string);
	#print;
	#print sub.dt.string;
	sub_ul = sub.next_sibling.next_sibling;

	# add integrated href
	for current_a in sub_ul.find_all('a'):
		tag = current_a;
		tag['href'] = "https://en.wikipedia.org" + current_a.get('href');

	#print sub_ul;
	for ul in sub_ul:
		content.append(ul);
		#print ul;
	#dl[0].append(content);
	topics[dl[count]] = content;
	count = count + 1;

#print topics;
print "~~~~~~~~";
for a in topics:
	print a;
	for x in topics[a]:
		print x;
	print;

# #print target_td.dl;