from django import forms

from product.models import Productmodel



class Productform(forms.ModelForm):
    
   class Meta:
       
       model=Productmodel

       fields="__all__"