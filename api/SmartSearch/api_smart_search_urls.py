from django.urls import path
from .api_smart_search_views import SmartSearch
urlpatterns = [
  path('', SmartSearch.as_view(), name='searching data'),
  ]