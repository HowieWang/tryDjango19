from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def posts_page(request):
    return render(request, "index.html", {})


def all(request):
    """
    return all list
    """
    obj_list = Post.objects.all()

    print(obj_list[0])
    content = {
        'obj_list': obj_list,
        'title': 'all list'
    }

    return render(request, 'index.html', content)
    # return HttpResponse("<h1>all list</h1>")


def create(request):
    # return HttpResponse("<h1>create</h1>")
    content = {
        'title': 'create'
    }

    return render(request, 'index.html', content)


def detail(request, id=None):
    # return HttpResponse("<h1>sublime detail</h1>")

    # 1. get a class
    # obj = Post.objects.get(id=id)  # does not exist? 
    obj = get_object_or_404(Post, id=id)
    print(type(obj))  # <class 'posts.models.Post'>

    # 2. return obj, without ''!!!!!
    content = {
        'title': 'detail-page',
        'obj': obj
    }

    return render(request, 'detail.html', content)


def update(request):
    # return HttpResponse("<h1>update 123</h1>")
    content = {
        'title': 'update'
    }

    return render(request, 'index.html', content)


def delete(request):
    # return HttpResponse("<h1>delete ---</h1>")
    content = {
        'title': 'delete'
    }

    return render(request, 'index.html', content)