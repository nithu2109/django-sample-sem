from django.urls import path
from . import views

urlpatterns=[path('',views.calorieinfo),
            path('result', views.result)]