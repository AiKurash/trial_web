from django.contrib import admin
from django.conf.urls import url
from .views import contactView, successView

app_name = 'sendemail'

urlpatterns = [
    url(r'^contact/$',contactView, name='contact'),
    url(r'^success/$',successView, name='success'),
]
