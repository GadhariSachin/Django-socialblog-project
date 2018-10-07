from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
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
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                     return redirect(request.POST.get('next'))
                else:
                     return redirect('article:postlist')
            else:
                return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

def UserLogoutView(request):
    logout(request)
    return redirect('article:postlist')

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


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
