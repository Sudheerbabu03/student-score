from django.urls import path # type: ignore
from student.views import *
urlpatterns=[
    path('',home,name="home"),
    path('grade/',grade,name='grade')
]