from django.conf.urls import url
from .api_display_data_default_views import Default
urlpatterns = [
  url('', Default.as_view(), name='getting_sort_by_view'),
]