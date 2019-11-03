from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def portfolios(request):
    articles = Article.objects.all().order_by("date") #orders articles by date
    return render(request,"portfolios.html",{'articles':articles})

def account(request):
    return render(request,'accounts.html')

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('account')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if request.method=="POST":
        auth_logout(request)
        return redirect('homepage')

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #save user for us
            #log user in
            login(request,user)
            return redirect('account')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

#Inside Account

@login_required(login_url="login")
def portfolio_create(request):
    return render(request,"portfolio_create.html")