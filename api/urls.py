from django.contrib import admin
from django.urls import path , include
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview" ),
    path('ebooklist/', views.ebookList, name="ebooklist" ),
    path('ebookspecific/<str:sk>/', views.ebookSpecific, name="ebookspecific" ),
    path('ebookcreate/', views.ebookCreate, name="ebookcreate" ),
    path('ebookupdate/<str:sk>/', views.ebookUpdate, name="ebookupdate" ),
    path('ebookdelete/<str:sk>/', views.ebookDelete, name="ebookdelete" ),

]