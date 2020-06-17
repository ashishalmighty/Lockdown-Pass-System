"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('citizen/', views.citizen, name='citizen'),
    path('citizen/request/', views.citReq, name='citizen/request'),
    path('citizen/status/', views.citStatus, name='citizen/status'),
    path('police/', views.police, name='police'),
    path('corporate/', views.corporate, name='corporate'),
    path('corporate/request/', views.corReq, name='corporate/request'),
    path('corporate/status/', views.corStatus, name='corporate/status'),
    path('authority/', views.authority, name='authority'),
    path('authority/approval/', views.approval, name='approval'),
    path('authority/bulk/', views.bulk, name='bulk'),
    path('authority/locality/', views.locality, name='locality'),
    path('authority/locality_set/', views.locality_set, name='locality_set'),
    path('authority/approve_corporate/', views.viewCorporateTable, name='approve_corporate'),
    path('authority/approve_corporate/approve/<id>', views.approveCom, name='approveCom'),
    path('authority/approve_corporate/reject/<id>', views.rejectCom, name='rejectCom'),
    path('authority/approve_citizen/', views.viewCitizenTable, name='approve_citizen'),
    path('authority/approve_citizen/approve/<id>', views.approveCit, name='approveCit'),
    path('authority/approve_citizen/reject/<id>', views.rejectCit, name='rejectCit'),
    path('essential/', views.essential, name='essential'),
    path('essential/request/', views.essReq, name='essential/request'),
    path('essential/status/', views.essStatus, name='essential/status'),
]
