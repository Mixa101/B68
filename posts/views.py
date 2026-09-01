from django.http.response import HttpResponse
from django.shortcuts import render

from posts.models import Post

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

    return render(r, "list_posts.html", {"posts": posts})
