from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_feed, name='search_feed'),
]
