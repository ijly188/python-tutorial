from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    # return HttpResponse("hi!!")
    # return HttpResponse("<h1>big</h1><h4>small</h4>")
    # return HttpResponse(status=404)
    return HttpResponseNotFound("tutorial Can't found.")

def articleList(request):
    return HttpResponse("tutorial Articles List")

def author(request):
    return render(request, "author.html")
