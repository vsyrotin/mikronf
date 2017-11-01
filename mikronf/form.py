from django import forms

class SubnetAddress(forms.Form):
    getAddress = forms.CharField(label='Set Subnet Address ', max_length=100)
