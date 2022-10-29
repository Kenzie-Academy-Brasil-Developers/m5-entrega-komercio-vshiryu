from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListCreate.as_view(), name="product"),
    path("products/<pk>/", views.ProductFilterUpdate.as_view(), name="product_id"),
]
