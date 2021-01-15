from django.urls import path
from . import views

urlpatterns=[
    path('',views.create_pawn, name='pawn'),
    path('customer/',  views.create_customer, ),
    #path('create_pawn/', views.create_pawn, name='pawn_form'),
    path('<int:pawn_id>/', views.detail_pawn),
    
]