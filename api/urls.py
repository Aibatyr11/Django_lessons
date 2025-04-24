from django.urls import path

from api.views import api_rubrics, api_rubric_details

app_name = 'api'

urlpatterns = [
    path('rubrics<int:pk>/', api_rubric_details),
    path('rubrics/', api_rubrics),
    ]