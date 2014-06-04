from alchemyapi import AlchemyAPI
import json

# def getCategory(demo_text):
# 	alchemyapi = AlchemyAPI()
# 	demo_text = unicode(demo_text);
# 	demo_text = demo_text.encode("ascii",'ignore');
# 	response = alchemyapi.entities('text', demo_text)

# 	if response['status'] == 'OK':
# 		#print(json.dumps(response, indent=4))
# 		if (not len(response['entities'])):
# 			category = []
# 			category.append("Undefined")
# 			return category

# 		entity = response['entities'][0]
# 		#print('text: ', entity['text'].encode('utf-8'))
# 		#print('type: ', entity['type'])
# 		#print('relevance: ', entity['relevance'])

# 		if entity.has_key('disambiguated') and entity['disambiguated'].has_key('subType'):
# 			category = entity['disambiguated']['subType']
# 		else:
# 			category = []
# 			category.append(entity['type'])
# 	else:
# 		category = []
# 		category.append("Undefined")
# 	return category

def getCategory(demo_text):
	demo_text = unicode(demo_text)
	demo_text = demo_text.encode("ascii",'ignore')
	#print demo_text
	category = []
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	knightCategories = requests.post("http://classify.knilab.com/classify/text/linear/",data="""input={text : '"""+demo_text+"""'}""",headers=headers).json()
	category.append(knightCategories[0][0])
	return category