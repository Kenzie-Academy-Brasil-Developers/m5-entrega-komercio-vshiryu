from rest_framework import permissions
from user.models import Account


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.method == "GET" or (
            request.user.is_authenticated and request.user.is_seller
        ):
            return True
        else:
            return False


class ProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or obj.seller == request.user:
            return True
        else:
            return False
