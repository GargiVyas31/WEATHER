from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.views.generic import View
from .forms import  CityForm, PlaceForm ,DataForm
from .models import City,Place,Data
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import AuthenticationForm

import jsonpickle,json
import serializers
import requests


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a848cab9299c77d2d845b7bbf1d306b5'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities= City.objects.all()
    weather_data=[]
    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather={
            'city':city.name,
            'temperature':r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather_app/index.html',context)

def sample(request):
    return render(request,'weather_app/sample.html')

def forecast(request):
    url='https://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=a848cab9299c77d2d845b7bbf1d306b5'


    if request.method=='POST':
        f1 = PlaceForm(request.POST)
        if f1.is_valid():
            f1.save()

        place= Place.objects.all()


        for p in place:
            rp = requests.get(url.format(p)).json()

            place_forecast={

            'temp_min':rp['list'][0]['main']['temp_min'],
            'temp_max':rp['list'][0]['main']['temp_max']
            }
            context={'place_forecast':place_forecast,'f1':f1}
            return render(request,'weather_app/sample.html',context)

    else:
        f1 = PlaceForm()
        return render(request,'weather_app/sample.html',{'f1':f1})


def data(request):

    url='https://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=a848cab9299c77d2d845b7bbf1d306b5'

    if request.method =='GET':
        f2 = DataForm()
        return render(request,'weather_app/sample.html',{'f2':f2})
    else:
        f2 = DataForm(request.POST)
        f2.save()

        data=[]

        c=Data.objects.count()
        city= Data.objects.filter(id=c)

        for city in city:
            rps = requests.get(url.format(city)).json()
            for i in rps['list']:
                print(i['main']['temp'])
                data.append(i['main']['temp'])


        context ={'data':data}


        return render(request, 'weather_app/chart.html',context)


def notify(request):
    user= request.user
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a848cab9299c77d2d845b7bbf1d306b5'
    r = requests.get(url.format('Mumbai')).json()

    if request.method=='GET':
        if request.user.is_authenticated:

            parameter={
                 'description':r['weather'][0]['description'],

                'user':user,
                'icon': r['weather'][0]['icon']

            }
            p= json.dumps({
                 'description':r['weather'][0]['description'],


                'icon': r['weather'][0]['icon']

            })
            return render(request,'weather_app/sample.html',{'p':p})
        else:

            parameter={

                'description':"Please register or login first",
                'icon': r['weather'][0]['icon']
                }

            return render(request,'weather_app/sample.html',parameter)





















