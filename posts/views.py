from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from .form import Search
from django.utils import timezone

# def post_list(request):
#     if request.method == 'GET':
#         post = Post.objects.order_by('-date')
#         return render(request, 'blog/posts.html', {'post':post})
    
def post_detail(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=id)
        return render(request, 'blog/post_details.html', {'post': post})
def post_filter(request):
    if request.method == 'GET':
        form = Search(request.GET)
        post = []
        if form.is_valid():
            query = form.cleaned_data['input']
            if Post.objects.filter(title__icontains=query):
                post = Post.objects.filter(title__icontains = query, date__lte=timezone.now()).order_by('-date')
            if Post.objects.filter(main_text__icontains = query):
                post = Post.objects.filter(main_text__icontains = query, date__lte=timezone.now()).order_by('-date')
        else:
            post =Post.objects.filter(date__lte=timezone.now()).order_by('-date')
        return render(request, 'blog/posts.html', {'search':form, 'post':post})