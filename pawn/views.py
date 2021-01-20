from django.shortcuts import render, get_object_or_404
from database.models import pawn,inventory
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.

def detail_pawn(request,pawn_id=None):
    pawn_list = get_object_or_404(pawn, pk= pawn_id)
    context={
        'pawn_list': pawn_list
    }
    return render(request, 'pawn_detail.html', context)

def create_pawn(request):
    if request.method=='POST':
        pawnform= pawn_form(request.POST)
        inventoryform= inventory_form(request.POST)

        if pawnform.is_valid() and inventoryform.is_valid():
            inventoryform.save()
            pawn=pawnform.save(commit=False)

            pawn.inventory_id = inventory.objects.latest('inventory_id')
            # pawn.inventory_id= raw_inventory
            pawn.save()
            
            
    else:
        pawnform=pawn_form()
        inventoryform=inventory_form(initial = {'operation': "p"})
    
    return render(request, 'pawn.html', {'pawn_form':pawnform, 'inventory_form':inventoryform })


def create_customer(request):
    if request.method=='POST':
        form= customer_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pawn/')

    else:
        form=customer_form()

    return render(request, 'customer.html',{'form': form })



