from alchemyapi import AlchemyAPI
import json
#demo_url = "http://www.nytimes.com/2014/05/17/world/asia/india-elections.html"

def getCategory(demo_text):
	alchemyapi = AlchemyAPI()
	demo_text = unicode(demo_text);
	demo_text = demo_text.encode("ascii",'ignore');
	response = alchemyapi.entities('text', demo_text)


	if response['status'] == 'OK':
		#print('## Response Object ##')
		#print(json.dumps(response, indent=4))
		if (not len(response['entities'])):
			category = []
			category.append("Undefined")
			return category

		#print('')
		#print('## Entities ##')
		entity = response['entities'][0]
		#print('text: ', entity['text'].encode('utf-8'))
		print('type: ', entity['type'])
		#print('relevance: ', entity['relevance'])

		if entity.has_key('disambiguated') and entity['disambiguated'].has_key('subType'):
			category = entity['disambiguated']['subType']
			print('subType: ', entity['disambiguated']['subType'])
		else:
			category = []
			category.append(entity['type'])
	else:
		#print('Error in entity extraction call: ', response['statusInfo'])
		#print 'error'
		category = []
		category.append("Undefined")
	#print type(category)
	return category