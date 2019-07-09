from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic

from user.forms import LoginForm, UserCreationForm
from user.utils import login_user


def login_user(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        cleaned_data = login_form.cleaned_data
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        login(request, user)
        if user:
            return redirect('project-list')
        else:
            print('error')
    return render(request, 'login.html', {'login_form': login_form})


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=user.email, password=password)
            print('>>> ', user)
            login(request, user)
            return redirect('project-list')
    return render(request, 'signup.html', {'form': form})

