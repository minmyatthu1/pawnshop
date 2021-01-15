from django.shortcuts import render

# Create your views here.

def receive_main(request):
    return render(request,'receive.html')