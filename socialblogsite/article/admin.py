# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'status')
    list_filter = ('status', 'created', 'updated', 'preference')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status',)
    date_hierarchy = 'created'

admin.site.register(Post, PostAdmin)
