from django.shortcuts import render
from . import models
# Create your views here.


def home(request):
    context={}
    return render(request,'index.html', context)

def about(request):
    context={}
    return render(request, 'about.html', context)
