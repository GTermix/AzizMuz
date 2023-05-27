from django import forms
from django.forms import ModelForm
from .models import *


class SubscribeNews(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = SubscribeEmail
        fields = '__all__'
