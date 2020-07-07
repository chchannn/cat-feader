from django.urls import path
from . import views

urlpatterns = [
    path('', views.button),
    path('fed', views.rotate_servo, name='rotate_servo') 
]


