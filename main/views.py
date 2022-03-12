from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'main/details/index.html', context)

def about(request):
    return render(request, 'main/details/about.html')
