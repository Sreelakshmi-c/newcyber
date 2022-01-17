from django.urls import path
from .import views
urlpatterns=[
    path('cyberr/',views.fnCyberr,name='cyberr/')
]