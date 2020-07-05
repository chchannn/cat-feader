from django.urls import path
from . import views

urlpatterns = [
    path('', views.rotate_servo, name='servo'), 
]


