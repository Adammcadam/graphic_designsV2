from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our-work', views.our_work, name='work'),
]
