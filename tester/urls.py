from django.urls import path
from tester.views import index, doctest

urlpatterns = [
    path('', index),
    path('doctest/', doctest),
]