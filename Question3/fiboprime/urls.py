from django.urls import path
from . import views

urlpatterns = [path('prime',views.prime),
               path('fibo',views.fibo),
               path('',views.main),
               path('nvalue',views.nvalue)]