from . import models
from django import forms

class createArticle(forms.ModelForm):
  class Meta:
    model = models.Article
    fields = ['title', 'body', 'slug', 'thumb']
