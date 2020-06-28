from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_quote, name='custom_quote'),
]
