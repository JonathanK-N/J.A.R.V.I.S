import requests
import json
import pyttsx3
import os
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    api_key = os.getenv('NEWS_API_KEY')
    url = f'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={api_key}'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

def getNewsUrl():
    api_key = os.getenv('NEWS_API_KEY')
    return f'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={api_key}'

if __name__ == '__main__':
    speak_news()
