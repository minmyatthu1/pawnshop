from django.shortcuts import render, get_object_or_404
from database.models import pawn
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def pawn_main(request):
    return render(request,'pawn.html', {})


def detail_pawn(request,pawn_id=None):
    pawn_list = get_object_or_404(pawn, pk= pawn_id)
    context={
        'pawn_list': pawn_list
    }
    return render(request, 'pawn_detail.html', context)

def create_pawn(request):
    if request.method=='POST':
        form= pawn_form(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=pawn_form()
    
    return render(request, 'pawn.html', {'form':form})

def create_customer(request):
    if request.method=='POST':
        form= customer_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pawn/')

    else:
        form=customer_form()

    return render(request, 'customer.html',{'form': form })

