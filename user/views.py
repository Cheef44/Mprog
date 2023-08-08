from django.shortcuts import render, redirect
from .form import UserReg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from posts.models import Post
from .models import UserStatus

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

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_accaunt(request, id):
    if request.method == "GET" and request.user.is_authenticated == True:
        user = get_object_or_404(User, id=id)
        post = Post.objects.filter(author__id =id).order_by('-date')
        user_status = UserStatus.objects.filter(user__id = id).order_by()
        return render(request, 'user_accaunt/user_accaunt.html', {'user':user, 'post':post, 'user_status':user_status})