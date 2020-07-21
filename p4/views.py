from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1>welcome to home</h1>")

def html_demo1(request):
    return render(request,"sample.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"reyaz",'name':"hello"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':100,'b':50})
