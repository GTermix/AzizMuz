from django import forms
from .models import *


class SubscribeNews(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',"class":"email-subscribe"}))

    class Meta:
        model = SubscribeEmail
        fields = '__all__'


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name','class':'m-a-i name-form'}),required=True)
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Number','class':'m-a-i number-form'}),required=True)
    comment = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'placeholder': 'Comment'}),required=True)

    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'comment']
