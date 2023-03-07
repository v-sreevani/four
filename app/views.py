from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sreevani(request):
    return HttpResponse('<h1> My name is Sreevani</h1>')

def maneesha(request):
    return HttpResponse('<marquee><h1>Maneesha Tinnava</marquee></h1>')
