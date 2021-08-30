from django.contrib import admin
from django.urls import path
import core.views
from .views import BlogListView


urlpatterns = [
    path('', core.views.index),
    path('nevs/', BlogListView.as_view(), name='nevs'),
]