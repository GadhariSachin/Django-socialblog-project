from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def UserLoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    if 'next' in request.POST:
                         return redirect(request.POST.get('next'))
                    else:
                         return redirect('article:postlist')
                else:
                    return HttpResponse("<h1> User is not active more!!")
    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

def UserLogoutView(request):
    logout(request)
    return redirect('article:postlist')

def UserSignupView(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit = False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user = new_user)
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


@login_required
def EditProfileView(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance = request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance = request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('article:postlist')
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'accounts/editprofile.html', context)
