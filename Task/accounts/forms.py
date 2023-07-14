from django import forms
from .models import Useraccount

class UseraccountForm(forms.ModelForm):
    class Meta:
        model=Useraccount
        fields="__all__"
        
        widgets={
            
            'name':forms.TextInput(attrs={'class':'form-control',"placeholder":"enter your name"}),
            
            'email':forms.EmailInput(attrs={'class':'form-control', "placeholder":"enter your email"}),
            

        }

