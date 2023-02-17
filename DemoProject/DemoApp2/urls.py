#"DemoApp2/urls.py"

from django.urls import path; #new
from DemoApp2 import views;
 
urlpattern=[
 path('third/',views.f3),
 path('fourth/',views,f4),
 ];