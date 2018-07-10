__author__ = 'DELL'
from django.urls import path
from .import views

app_name ="weather_app"
urlpatterns = [

    path('', views.sample, name='sample'),
    path('index', views.index, name='index'),
    path('forecast',views.forecast,name='forecast'),
    path('graph',views.data,name="data"),
    path('notify',views.notify,name='notify'),


]

