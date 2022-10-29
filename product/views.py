from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from product.models import Product
from product.permissions import IsSeller, ProductOwner
from product.serializer import ProductGeneralSerializer, ProductSerializer
from utils.mixins import SerializerByMethodMixin

# Create your views here.


class ProductListCreate(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSeller]

    serializer_map = {
        "GET": ProductGeneralSerializer,
        "POST": ProductSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductFilterUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProductOwner]
    serializer_class = ProductSerializer
