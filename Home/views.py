from django.shortcuts import render , HttpResponse
from .models import *
from Codekaro import settings
# Create your views here.
def home(request):
    return render(request , 'base.html')

def brainf(request):
    brains = brain.objects.all()
    params = {'questions' : brains}
    return render(request , 'brain.html' , params)

def beginnerf(request):
    return render(request , 'base.html')

def brutef(request):
    return render(request , 'base.html')

def greedf(request):
    return render(request , 'base.html')

def subf(request):
    return render(request , 'base.html')

def implementf(request):
    return render(request , 'base.html')

def sortf(request):
    return render(request , 'base.html')

def binaryf(request):
    return render(request , 'base.html')

def pointerf(request):
    return render(request , 'base.html')

def hashf(request):
    return render(request , 'base.html')

def pairf(request):
    return render(request , 'base.html')

def dpstandf(request):
    return render(request , 'base.html')

def dpf(request):
    return render(request , 'base.html')

def treef(request):
    return render(request , 'base.html')

def graphf(request):
    return render(request , 'base.html')

def dsuf(request):
    return render(request , 'base.html')

def segtreef(request):
    return render(request , 'base.html')