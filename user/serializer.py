from dataclasses import fields
from rest_framework import serializers
from user.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_seller",
            "is_superuser",
            "date_joined",
            "is_active",
        ]
        read_only_fields = [
            "id",
            "is_superuser",
            "date_joined",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class AccUpdateSerializer(serializers.ModelSerializer):
    ...
