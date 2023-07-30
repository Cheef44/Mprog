from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from .form import Search
from .form import PostEdit
from .form import UserReg
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

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

def user_registration(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            form = form.save(commit=False)          
            form.save()
            return redirect('post_list')
    else:
        form = UserReg()
    return render(request, 'registration/registration.html', {'user_form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
    return render(request, 'registration/login.html')