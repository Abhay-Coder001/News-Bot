#News
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Good Morning sir this is news for today.. Lets begin sir")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=55b65b675ac744069291bab99306f7a9"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..sir")

    speak("Thanks for listening...Sir")
