from django import forms 
from django.forms import ModelForm
from database.models import *
from .widgets import DatePicker

class customer_form(forms.ModelForm):
    class Meta:
        model=customer
        fields= ['name', 'address', 'point', 'comment']
        widgets = {
        'name': forms.TextInput(attrs={'man class': 'form-control','placeholder': 'Customer'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'point': forms.TextInput(attrs={'class': 'form-control'}),
        'comment':forms.Textarea(attrs={'rows':4, 'cols':20}),
        
    }




class pawn_form(forms.ModelForm):
   # pawn_amt= forms.IntegerField()
    class Meta:
        model=pawn
        fields=['customer_id', 'invoice_number', 'pawn_amt','pawn_date']
        widgets = {
        'customer_id': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Customer ID'}),
        # 'inventory_id': forms.TextInput(attrs={'class': 'form-control'}),
        'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
        'pawn_amt':forms.NumberInput(attrs={'class':'form-control'}),
        'pawn_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        'created_time' : forms.DateTimeInput(attrs={'class': 'datepicker'}),
    }

     

class inventory_form(forms.ModelForm):
   # pawn_amt= forms.IntegerField()
    class Meta:
        model=inventory
        fields=['inventory_id', 'item_name', 'item_type','weight', 'operation', 'comment']
        widgets = {
        'inventory_id': forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
        'item_name': forms.TextInput(attrs={'class': 'form-control'}),
        'item_type': forms.TextInput(attrs={'class': 'form-control'}),
        'weight':forms.TextInput(attrs={'class':'form-control'}),
        'operation':forms.TextInput(attrs={'class':'form-control'}),
    }
