from django.urls import path
from tester.views import index

urlpatterns = [
    path('', index),
]