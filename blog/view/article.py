from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def articleList(request):
    return HttpResponse("tutorial Articles List")

def author(request):
    return render(request, "author.html")
