import json
import requests

class news:
    emp = 0
    def __init__(self, jsonUrl):
        self.url = jsonUrl
    def jsonParse(self):

        newsApi=requests.get(self.url)
        dump = newsApi.json()
        json_str = json.dumps(dump)
        resp = json.loads(json_str)
        for index in range(0,9):
            context = {"title" + str(index): resp["articles"][index]["title"],
                       "urlToImage" + str(index): resp["articles"][index]["urlToImage"],
                       "url" + str(index): resp["articles"][index]["url"],
                       "desp" + str(index): resp["articles"][index]["description"]}
            print(context)

url='https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=606014a906f14ea59a48b33381c5f972'
xr = news(url)
xr.jsonParse()