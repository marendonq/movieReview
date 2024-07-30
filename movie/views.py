from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
    #return HttpResponse('<h1>si funciona</h1>')
    return render(request, 'home.html',{'name':'Miguel Rendon'})

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')