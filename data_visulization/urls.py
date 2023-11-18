# chart_app/urls.py

from django.urls import path
from .views import upload_csv, chart

urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('chart/', chart, name='chart'),
]
