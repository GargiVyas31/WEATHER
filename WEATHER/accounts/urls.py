__author__ = 'DELL'
from django.conf.urls import url
from .import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
       path('register/',views.register_view,name='register'),
       path('login/',views.login_view,name='login'),
       path('logout/',views.logout_view,name='logout'),
       path('signup/',views.signup,name='signup'),
       url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]