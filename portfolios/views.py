from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def portfolios(request):
    articlesStorage = Article.objects.all().order_by("date") #orders articles by date
    return render(request,"portfolios.html",{'articles':articlesStorage})