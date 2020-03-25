from django.urls import path
from .api_get_paginated_views import SortBy ,Count
urlpatterns = [
  path('<int:page>/', SortBy.as_view(), name='getting_sort_by_view'),
  path('count/', Count.as_view(), name= 'get_total_pages_count')
  ]