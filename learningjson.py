import requests
import json

foo = requests.get(url='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=132c562158c648fabf3e9ca22e64d635')
json_news=foo.json()

json_obj=json.dumps(json_news)
json_dict=json.loads(json_obj)
print(json_dict['articles'][2]['title'])
print(json_dict['articles'][2]['description'])

path='E:\Sgraph Python practice\detailapi.txt'
dataW=open(path,'w')

dataW.write('')
dataW.close()