from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='shop'),
    path('<product_id>', views.product_page, name='product_page'),
]