from django.shortcuts import render
from goods.models import Categories

def index(request):


    context = {
        "title": "The Book Haven - Main",
        'content': 'Shop in style - Main',
        'description': 'With this shop hompeage templates',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "The Book Haven - About us",
        'content': 'Shop in style - About us',
        'description': "Welcome to The Book Haven – Your Literary Escape!"
    }
    return render(request, 'main/about.html', context)
