# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required

# Create your views here.

def PostListView(request):
    posts = Post.objects.all().filter(status__iexact="published")
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query)|
            Q(body__icontains=query)|
            Q(author_id__username=query)|
            Q(preference__icontains=query)
        )
    context =  {'post':posts}
    return render(request, 'article/post_list.html', context)



def PostDetailView(request, id, slug):
    post =get_object_or_404(Post, id=id, slug=slug)
    is_liked = False
    if post.like.filter(id=request.user.id).exists():
        is_liked =True
    context ={
        'post': post,
        'is_liked' : is_liked,
        'likes_count':post.likes_count(),
        }
    return render(request, 'article/post_detail.html', context)


def PostEditView(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        raise Http404()
    if request.method == 'POST':
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
        context = {
            'post':post,
            'form':form,
        }
        return render(request, 'article/post_edit.html', context)


def LikePostView(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        is_liked = False
    else:
        post.like.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url ="/accounts/login")
def PostCreateView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('article:postlist')
    else:
        form = PostCreateForm()
        context = {'form':form}
        return render(request, 'article/post_create.html', context)

def PostDeleteView(request, id):
        post = get_object_or_404(Post, id=id)
        if post.author != request.user:
            raise Http404()
        post.delete()
        return redirect('article:postlist')
