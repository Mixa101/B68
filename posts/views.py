from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm
from posts.models import Category, Post, Tag

# Create your views here.


def hello_world(r):
    return HttpResponse("<h1>Hello world!</h1>")


def my_name(r):
    name = "Islam"

    return HttpResponse(f"<h2> Hello </h2> <h1>{name}</h1>")


def say_name(r, name):
    return HttpResponse(f"<h2> Hello </h2> <h1>{name}</h1>")


def post_list(r):
    posts = Post.objects.all()

    return render(r, "posts/list_posts.html", {"posts": posts})


def post_detail(r, pk):
    post = get_object_or_404(Post, id=pk)
    post.views += 1
    post.save()
    return render(r, "posts/post_detail.html", {"post": post})


def create_post(request: HttpRequest) -> HttpResponse:
    form = PostForm()
    if request.method.lower() == "post":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=form.instance.pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        "posts/create_post.html",
        {"form": form, "tags": tags, "categories": categories},
    )
