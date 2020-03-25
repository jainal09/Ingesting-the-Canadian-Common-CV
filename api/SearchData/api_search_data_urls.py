from django.urls import path
from .api_search_data_views import Search
urlpatterns = [
  path('', Search.as_view(), name='searching data'),
  ]