__author__ = 'DELL'
from  django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm , TextInput
from .models import City ,Place, Data



class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets= {'name':TextInput(attrs={'class': "input" ,'placeholder': "City Name"})}





class PlaceForm(ModelForm):
    choices=[('Las Vegas','Las Vegas'),('Punjab','Punjab'),('Sacramento','Sacramento')]
    place= forms.CharField(label='Place',widget=forms.Select(choices=choices))
    class Meta:
        model =Place
        fields = ['place']

class DataForm(ModelForm):
    city=forms.CharField()
    class Meta:
        model= Data
        fields=['city']







