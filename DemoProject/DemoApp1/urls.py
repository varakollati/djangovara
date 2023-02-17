#"DemoApp1/urls.py"

from django.urls import path; #new
from DemoApp1 import views;
 
urlpattern=[
 path('first/',views.f1),
 path('second/',views,f2),
 