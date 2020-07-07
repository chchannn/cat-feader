from django.shortcuts import render

from . import feed

# def rotate_servo(request):
#         feed.feed(2.5, 8.5)
#         return render(request, 'feeder/home.html')

def button(request):

        return render(request, 'feeder/home.html')


def rotate_servo(request):

        info = feed.feed(2.5, 8.5)
        #Do your stuff ,calling whatever you want from set_gpio.py

        return render(request, 'feeder/home.html', {'data':info})