from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def homepage(request):
    articles = Article.objects.all().order_by("date")  # orders articles by date
    return render(request,"homepage.html",{'articles':articles})
def portfolios(request):
    articles = Article.objects.all().order_by("date") #orders articles by date
    return render(request,"portfolios.html",{'articles':articles})