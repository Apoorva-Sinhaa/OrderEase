from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'First Name',
            'lname' : 'Last Name.' ,
            'price' : 'Price' ,
            'mail' : 'Email ID',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg. Apoorva'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'eg. Sinha'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'eg. 1000.00'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'eg. IN'}),
        }
