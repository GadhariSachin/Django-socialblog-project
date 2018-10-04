# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    PREFER_CHOICES= (
        ('All', 'All'),
        ('Sports', 'Sports'),
        ('Politics', 'Politics'),
        ('Technology', 'Technology'),
        ('Movies', 'Movies'),
        ('Vehicle', 'Vehicles'),
    )
    title = models.CharField(max_length = 256)
    slug = models.SlugField(max_length = 128, default='new-article' )
    author = models.ForeignKey(User, related_name='article_posts')
    body = models.TextField()
    like = models.ManyToManyField(User, blank=True, related_name='likes')
    image = models.ImageField(default = 'default.jpg', blank=True)
    preference = models.CharField(max_length=10, choices=PREFER_CHOICES, default='all')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def snippet(self):
        return self.body[:100] + '...'

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.like.count()

    def get_absolute_url(self):
        return reverse("article:postdetail", args=[self.id, self.slug])

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
