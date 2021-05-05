from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    return HttpResponse("<h1>THIS IS THE HOMEPAGE</h1>")

def ok(request):
    return render(request, 'base.html')