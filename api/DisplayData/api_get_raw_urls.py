from django.conf.urls import url
from .api_get_raw_views import SortBy
urlpatterns = [
  url('', SortBy.as_view(), name='getting_sort_by_view'),
]