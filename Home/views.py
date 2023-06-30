from django.shortcuts import render , HttpResponse
from .models import *
from Codekaro import settings
# Create your views here.
def home(request):
    return render(request , 'base.html')

def brainf(request):
    brains = brain.objects.all().order_by('order')
    params = {'questions' : brains}
    return render(request , 'brain.html' , params)

def beginnerf(request):
    beginners = beginner.objects.all().order_by('order')
    params = {'questions' : beginners}
    return render(request , 'brain.html' , params)

def brutef(request):
    brutes = brute.objects.all().order_by('order')
    
    params = {'questions' : brutes}
    return render(request , 'brain.html' , params)

def greedf(request):
    greeds = greed.objects.all().order_by('order')
    params = {'questions' : greeds}
    return render(request , 'brain.html' , params)

def subf(request):
    subs = sub.objects.all().order_by('order')
    params = {'questions' : subs}
    return render(request , 'brain.html' , params)

def implementf(request):
    implements = implement.objects.all().order_by('order')
    params = {'questions' : implements}
    return render(request , 'brain.html' , params)

def sortf(request):
    sorts = sort.objects.all().order_by('order')
    params = {'questions' : sorts}
    return render(request , 'brain.html' , params)

def binaryf(request):
    binaries = binary.objects.all().order_by('order')
    params = {'questions' : binaries}
    return render(request , 'brain.html' , params)

def pointerf(request):
    pointers = pointer.objects.all().order_by('order')
    params = {'questions' : pointers}
    return render(request , 'brain.html' , params)

def hashf(request):
    hashs = hash.objects.all().order_by('order')
    params = {'questions' : hashs}
    return render(request , 'brain.html' , params)

def pairf(request):
    pairs = pair.objects.all().order_by('order')
    params = {'questions' : pairs}
    return render(request , 'brain.html' , params)

def dpstandf(request):
    dpstands = dpstand.objects.all().order_by('order')
    params = {'questions' : dpstands}
    return render(request , 'brain.html' , params)

def dpf(request):
    dps = dp.objects.all().order_by('order')
    params = {'questions' : dps}
    return render(request , 'brain.html' , params)

def treef(request):
    trees = tree.objects.all().order_by('order')
    params = {'questions' : trees}
    return render(request , 'brain.html' , params)

def graphf(request):
    graphs = graph.objects.all().order_by('order')
    params = {'questions' : graphs}
    return render(request , 'brain.html' , params)

def dsuf(request):
    dsus = dsu.objects.all().order_by('order')
    params = {'questions' : dsus}
    return render(request , 'brain.html' , params)

def segtreef(request):
    segtrees = segtree.objects.all().order_by('order')
    params = {'questions' : segtrees}
    return render(request , 'brain.html' , params)