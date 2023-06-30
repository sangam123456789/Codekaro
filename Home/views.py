from django.shortcuts import render , HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request , 'base.html')

def brain(request):
    return render(request , 'base.html')

def beginner(request):
    return render(request , 'base.html')

def brute(request):
    return render(request , 'base.html')

def greed(request):
    return render(request , 'base.html')

def sub(request):
    return render(request , 'base.html')

def implement(request):
    return render(request , 'base.html')

def sort(request):
    return render(request , 'base.html')

def binary(request):
    return render(request , 'base.html')

def pointer(request):
    return render(request , 'base.html')

def hash(request):
    return render(request , 'base.html')

def pair(request):
    return render(request , 'base.html')

def dpstand(request):
    return render(request , 'base.html')

def dp(request):
    return render(request , 'base.html')

def tree(request):
    return render(request , 'base.html')

def graph(request):
    return render(request , 'base.html')

def dsu(request):
    return render(request , 'base.html')

def segtree(request):
    return render(request , 'base.html')