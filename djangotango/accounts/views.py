from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserFormCreate
from django.contrib import messages

# Create your views here.

def signup_view(request):
  if request.method == 'POST':
    form = UserFormCreate(request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request, f'<strong>Success !&nbsp;</strong> Account created for {user }')
      login(request, user)
      return redirect('articles:list')
  else:
    form = UserFormCreate()
  return render(request, 'accounts/signup.html', {'form': form} )


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request , user)
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      return redirect('articles:list')
  else:
    form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
  if request.method=='POST':
    logout(request)
    return redirect('articles:list')
