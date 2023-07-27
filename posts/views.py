from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    if request.method == 'GET':
        post = Post.objects.order_by('-date')
        return render(request, 'blog/posts.html', {'post':post})