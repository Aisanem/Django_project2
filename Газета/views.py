from django.shortcuts import render
from.models import Post, Comments


def index(request):
    
    return render(request, 'news/index.html')
