from django.urls import path
from .import views
urlpatterns=[
    path('',views.fnCyberr,name='cyberr/')
]