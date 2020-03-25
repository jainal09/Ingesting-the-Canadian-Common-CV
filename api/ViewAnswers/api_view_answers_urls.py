from django.urls import path
from .api_view_answers_views import AnswersId, AnswersTitle
urlpatterns = [
  path('id/', AnswersId.as_view(), name='searching data'),
  path('title/', AnswersTitle.as_view(), name='searching data'),
  ]