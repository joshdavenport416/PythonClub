from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),    
    path('meetingsdetail/<int:id>', views.meetingsdetail, name='meetingsdetail'),
    path('newresource/', views.newresource, name='newresource'),
    path('newmeeting/', views.newmeeting, name='newmeeting'),
]