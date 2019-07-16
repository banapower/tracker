from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from tracker.utils.utils import close_view
from user.forms import LoginForm, UserCreationForm, UserEditForm


def login_user(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        cleaned_data = login_form.cleaned_data
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('project-list')
        else:
            print('error')
    return render(request, 'login.html', {'login_form': login_form})


def signup(request):
    form = UserCreationForm(request.POST or None, request.FILES or None)
    if request.POST:
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=user.email, password=password)
            if user:
                login(request, user)
                return redirect('project-list')
    return render(request, 'signup.html', {'form': form})


@login_required
def edit(request):
    form = UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
        return close_view(request, 'project-list')
    return render(request, 'edit.html', {'form': form})
