from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, logout
from .forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

def index(request):
    template = "main_part/index.html"
    return render(request, template)

def user_login(request):
    template = "main_part/login.html"
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def user_logout(request):
    logout(request)
    return redirect('user_login')


def create_user(request):
    template = "main_part/create_user.html"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировали нового пользователя')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def all_users(request):
    template = "main_part/all_users.html"
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, template, context)

def delete_user(request, user_id):
    template = "main_part/delete_user.html"
    user_del = User.objects.get(id=user_id)
    context = {
        'user_del': user_del,
    }
    if request.method == 'POST':
        user_del.delete()
        return redirect(all_users)
    return render(request, template, context)


def edit_user(request, user_id):
    template = "main_part/edit_user.html"
    user_edit = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserChangeCustomFort(request.POST, instance=user_edit)
        if form.is_valid():
            form.save()
            return redirect(all_users)
    else:
        form = UserChangeCustomFort(instance=user_edit)

    context = {
        'form': form,
        'user_edit': user_edit,
        'user_id': user_id,
    }

    return render(request, template, context)

def edit_user_password(request, user_id):
    template = "main_part/edit_user_password.html"
    user_edit = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserPasswordFort(request.POST, instance=user_edit)
        if form.is_valid():
            form.save()
            return redirect(all_users)
    else:
        form = UserPasswordFort(instance=user_edit)

    context = {
        'form': form,
        'user_edit': user_edit,
    }

    return render(request, template, context)

def create_entry(request):
    template = "main_part/create_entry.html"
    if request.method == 'POST':
        form = MainDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MainDataForm()
    context = {
        'form': form,
    }
    return render(request, template, context)
