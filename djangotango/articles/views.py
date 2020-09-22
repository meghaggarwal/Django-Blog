from django.shortcuts import render, redirect
from .import views
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.

def article_list(request):
  articles = Article.objects.all().order_by('date')
  return render(request, 'articles/article_list.html', {'articles': articles})

def article_details(request, slug):
  article = Article.objects.get(slug = slug)
  return render(request, 'articles/article_detail.html', {'article': article})
  # return HttpResponse(slug)

@login_required(login_url="/accounts/login/")
def article_create(request):
  if request.method == 'POST':
    form = forms.createArticle(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('articles:list')
  else:
    form = forms.createArticle()
  return render(request, 'articles/article_create.html', {'form':form})


