from django.shortcuts import render, redirect
from .form import UserReg
from django.contrib.auth import authenticate, login, logout
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