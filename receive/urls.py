from django.urls import path
from . import views

urlpatterns=[
    path('', views.receive_main,name='receive')
]