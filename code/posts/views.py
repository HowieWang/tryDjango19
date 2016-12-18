from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_page(request):
    return HttpResponse("<h1>sublime python</h1>")


def all(request):
    return HttpResponse("<h1>all list</h1>")


def detail(request):
    return HttpResponse("<h1>sublime detail</h1>")


def update(request):
    return HttpResponse("<h1>update 123</h1>")


def delete(request):
    return HttpResponse("<h1>delete ---</h1>")