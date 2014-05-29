from alchemyapi import AlchemyAPI
import json, requests

# def getCategory(demo_text):
# 	alchemyapi = AlchemyAPI()
# 	demo_text = unicode(demo_text);
# 	demo_text = demo_text.encode("ascii",'ignore');
# 	response = alchemyapi.taxonomy('text', demo_text)

# 	if response['status'] == 'OK':
# 		print(json.dumps(response, indent=4))
# 		entity = response['taxonomy'][0]
# 		category = []
# 		category.append(entity['label'])
# 	else:
# 		print('Error in taxonomy call: ', response['statusInfo'])
# 		category = []
# 		category.append("Undefined")
# 	print category
# 	return category

def getCategory(demo_text):
	#print demo_text
	category = []
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	knightCategories = requests.post("http://classify.knilab.com/classify/text/linear/",data="""input={text : '"""+demo_text+"""'}""",headers=headers).json()
	category.append(knightCategories[0][0])
	return category