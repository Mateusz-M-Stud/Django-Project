from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:list_id>/add/', views.add_product, name='add_product'),
    path('list/<int:list_id>/', views.shopping_list_detail, name='shopping_list_detail'),
]
