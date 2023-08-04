from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from .form import Search
from .form import PostEdit
from django.utils import timezone
from user.form import UserCommentsForm
from user.models import UserComments

# def post_list(request):
#     if request.method == 'GET':
#         post = Post.objects.order_by('-date')
#         return render(request, 'blog/posts.html', {'post':post})

#В данной функции происходит вывод детального поста и комментариев к посту, а также создание комментариев
def post_detail(request, id):
    if request.method == 'GET' or request.method == 'POST':
        post = get_object_or_404(Post, pk=id)
        comment = UserCommentsForm(request.POST)
        comment_information = UserComments.objects.filter(post__pk = id)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.user = request.user
            comment.date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('post_detail', id=id)
        else:
            comment = UserCommentsForm() 
        return render(request, 'blog/post_details.html', {'post': post, 'comment':comment, 'comment_information':comment_information})
   
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

def post_create(request):
    if request.method == 'POST':
        form = PostEdit(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.date = timezone.now()
            form.save()
            return redirect('post_detail', id=form.pk)
    else:
        form = PostEdit()
    return render(request, 'blog/post_create.html', {'form':form})

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostEdit(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.date = timezone.now()
            form.save()
            return redirect('post_detail', id=form.pk)
    else:
        form = PostEdit(instance=post)
    return render(request, 'blog/post_create.html', {'form':form})