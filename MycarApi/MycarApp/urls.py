from django.conf.urls import url
from MycarApp import views

urlpatterns=[
    url(r'^car$', views.carApi),
    url(r'^car/([0-9]+)$', views.carApi)
]