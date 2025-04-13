from django import forms
from .models import firstappVarity

class FirstAppForm(forms.Form):
    app_varity = forms.ModelChoiceField(queryset=firstappVarity.objects.all(), label="Select App Varity")
    #app_varity = forms.CharField(max_length=100, label="App Varity", required=True)