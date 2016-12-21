from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_page(request):
    return render(request, "index.html", {})


def all(request):
    content = {
        'title':'all list'
    }

    return render(request, 'index.html', content)
    # return HttpResponse("<h1>all list</h1>")

def create(request):
    # return HttpResponse("<h1>create</h1>")
    content = {
        'title':'create'
    }

    return render(request, 'index.html', content)


def detail(request):
    # return HttpResponse("<h1>sublime detail</h1>")
    content = {
        'title':'detail'
    }

    return render(request, 'index.html', content)

def update(request):
    # return HttpResponse("<h1>update 123</h1>")
    content = {
        'title':'update'
    }

    return render(request, 'index.html', content)

def delete(request):
    # return HttpResponse("<h1>delete ---</h1>")
    content = {
        'title':'delete'
    }

    return render(request, 'index.html', content)