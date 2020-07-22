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

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))  
      
def ab(request, ab):
    gre = list(map(int, ab.split(" ")))
    return HttpResponse(f"<h1>Maximum num is: {max(gre)}</h1>")
def gre(request,num):
    a=num.split(" ")
    if int(a[0])>int(a[1]):
        gre=int(a[0])
    else:
        gre=int(a[1])
    res=gre
    return HttpResponse(str(res))
 
