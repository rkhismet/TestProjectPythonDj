from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
  return render(request, 'gen/home.html')

def password(request):
  characters = list('abcdefghijklmnopqrstuvwxyz')
  num_special = 0
  if request.GET.get('special') == 'on':
    characters.extend(',./;[]}{!@#$%^&*()_+=-±§`~')   
  if request.GET.get('uppercase') == 'on':
    characters.extend('0123456789')   
  if request.GET.get('special') == 'on':
    characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   
  
  length = int(request.GET.get('length', 12))
  password = ''
  for x in range(length):
    password += random.choice(characters)

  return render(request, 'gen/password.html', {'password' : password})

def about(request):
  return render(request, 'gen/about.html')