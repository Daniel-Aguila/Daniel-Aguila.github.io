from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def portfolios(request):
    articles = Article.objects.all().order_by("date") #orders articles by date
    return render(request,"portfolios.html",{'articles':articles})
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #save user for us
            #log user in
            return redirect('portfolios:homepage')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})