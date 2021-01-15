from django import forms 
from django.forms import ModelForm
from database.models import *

class customer_form(forms.ModelForm):
    class Meta:
        model=customer
        fields= ['name', 'address', 'point', 'comment']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Customer'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'point': forms.TextInput(attrs={'class': 'form-control'}),
        'comment':forms.Textarea(attrs={'rows':4, 'cols':20}),
        
    }




class pawn_form(forms.ModelForm):
   # pawn_amt= forms.IntegerField()
    class Meta:
        model=pawn
        fields=['customer_id', 'inventory_id', 'invoice_number', 'pawn_amt',]
        widgets = {
        'customer_id': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Customer'}),
        'inventory_id': forms.TextInput(attrs={'class': 'form-control'}),
        'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
        'pawn_amt':forms.NumberInput(attrs={'class':'form-control'}),
        # 'pawn_date': forms.DateTimeInput(attrs={'class': 'form-control',}),
    }

     
