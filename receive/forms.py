from database.models import receive
from django import forms 
from django.forms import ModelForm 


class receive_form(forms.ModelForm):
   
    class Meta:
        model=receive
        fields=['inventory_id', 'receive_date', 'month_different','interest', 'receive_total_amt']
        widgets = {
        'inventory_id': forms.TextInput(attrs={'class': 'form-control'}),
        'receive_date': forms.DateInput(attrs={'type': 'date'}),
        'month_different':forms.NumberInput(attrs={'class':'form-control'}),
        'interest': forms.NumberInput(attrs={'class':'form-control'}),
        'receive_total_amt' : forms.NumberInput(attrs={'class':'form-control'}),
        }