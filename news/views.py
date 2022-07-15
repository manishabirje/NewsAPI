from urllib import response
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import requests


def index(request):
    q = request.GET.get('q')
    response = requests.get(f'https://newsapi.org/v2/everything?q={q}&from=2022-07-13&sortBy=popularity&apiKey=8b0032172736412b8526ec635e4be2d0')
    data = response.json()
    articles = data['articles']
    context= {'articles': articles }
    return render(request,'news/index.html' ,context)

