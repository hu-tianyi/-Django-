from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime


# Create your views here.
def home(request):
    post_list = Article.objects.all()  # get all of the Article object
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    return HttpResponse("You're looking at %s." % id)

def test(request) :
        return render(request, 'test.html', {'current_time': datetime.now()})

