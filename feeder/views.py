from django.shortcuts import render
from django.http import HttpResponse

from . import feed

def rotate_servo(request):
        feed.feed(2.5, 8.5)
        return HttpResponse('Food dispensed!')
# Create your views here.
