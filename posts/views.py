from django.shortcuts import render, get_object_or_404
from .models import Post


def display_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/detail.html", context={"post": post})
