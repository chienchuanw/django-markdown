from django.shortcuts import render
from .models import Post
import markdown


def display_post(request):
    md = markdown.Markdown(extensions=["fenced_code"])
    post = Post.objects.first()
    post.content = md.convert(post.content)
    return render(request, "posts/detail.html", context={"post": post})
