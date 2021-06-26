from django.shortcuts import render
from common.models import *

def home(request):
    return render(request,'home.html')
