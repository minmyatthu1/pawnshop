from django.shortcuts import render
from .forms import receive_form

# Create your views here.

def create_receive(request):
    if request.method=='POST':
        form= receive_form(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/pawn/')

    else:
        form=receive_form()

    return render(request, 'receive.html',{'form': form })