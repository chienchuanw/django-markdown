from django.shortcuts import render
from .models import Post


def display_post(request):
    post = Post.objects.first()
    return render(request, "posts/detail.html", context={"post": post})
