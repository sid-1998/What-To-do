from django import forms
from app.models import List

class ListForm(forms.ModelForm):
    text=forms.CharField(label='Todo',widget= forms.TextInput(attrs={ 'placeholder':'Enter a Todo'}))
    class Meta:
        model = List
        fields = ['text']
