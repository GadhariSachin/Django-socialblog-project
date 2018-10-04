from . import models
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "image", "preference", "status"]

class PostEditForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "image", "preference", "status"]
