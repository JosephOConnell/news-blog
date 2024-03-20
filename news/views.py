from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv, dotenv_values
from newsapi import NewsApiClient

load_dotenv()
API = os.getenv('NEWS_API')

def index(request):
    url = (f"https://newsapi.org/v2/everything?q=gaming, gaming-news, video-games&apiKey={API}")
    gaming_news = requests.get(url).json()
    a = gaming_news['articles']

    urlToImage = []
    author = []
    title = []
    description = []
    url = []

    for i in range(len(a)):
        f = a[i]
        urlToImage.append(f['urlToImage'])
        author.append(f['author'])
        title.append(f['title'])
        description.append(f['description'])
        url.append(f['url'])
    news_list = zip(urlToImage, author, title, description, url)
    
    context = {'news_list': news_list}

    return render(request, 'news/news.html', context)
