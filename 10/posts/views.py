from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
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
    # check the POST
    form = PostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get('title'))
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'post saved')
        messages.success(request, 'post saved, again', extra_tags='a new tag here')
        
    # if request.method == 'POST':
    #     print('content', request.POST.get('content'))
    #     print('title', request.POST.get('title'))
    #     # Post.objects.create(title=...)
    else:
        messages.error(request, 'error post')

    content = {
        'form': form
    }

    return render(request, 'form.html', content)


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


def update(request, id=None):
    # return HttpResponse("<h1>update 123</h1>")
    obj = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        print(form.cleaned_data.get('title'))
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'post saved')

    content = {
        'title': 'update',
        'form': form
    }

    return render(request, 'form.html', content)


def delete(request, id=None):
    # return HttpResponse("<h1>delete ---</h1>")
    obj = get_object_or_404(Post, id=id)
    obj.delete()
    messages.success(request, "delete successfully")
    return redirect("list")
