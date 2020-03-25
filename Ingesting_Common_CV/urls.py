"""Ingesting_Common_CV URL Configuration

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
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('default/', include('api.DisplayDataDefault.api_display_data_default_urls')),
    path('data/', include('api.DisplayData.api_get_raw_urls')),
    path('pages/', include('api.DisplayDataPaginated.api_get_paginated_urls')),
    path('search/', include('api.SearchData.api_search_data_urls')),
    path('answers/', include('api.ViewAnswers.api_view_answers_urls')),
    path('smart_search/',include('api.SmartSearch.api_smart_search_urls'))
]
