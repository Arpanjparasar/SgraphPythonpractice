from flask import Flask,render_template
import requests
import json




app = Flask(__name__)

@app.route('/')
def hello():
    foo = requests.get(
    url='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=132c562158c648fabf3e9ca22e64d635')
    json_news = foo.json()

    json_obj = json.dumps(json_news)
    json_dict = json.loads(json_obj)
    headlines=json_dict['articles'][2]['title']
    description=json_dict['articles'][2]['description']
    print(json_dict['articles'][2]['title'])
    print(json_dict['articles'][2]['description'])

    return render_template('index.html',headlines=headlines,desc=description)


if (__name__ == "__main__"):
    app.run(debug=True)
