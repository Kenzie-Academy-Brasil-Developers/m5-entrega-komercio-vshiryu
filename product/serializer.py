from rest_framework import serializers

from product.models import Product
from user.serializer import AccountSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]
        seller = AccountSerializer(read_only=True)


class ProductGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller_id",
        ]
