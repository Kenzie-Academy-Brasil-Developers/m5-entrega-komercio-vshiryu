from rest_framework import permissions
from user.models import Account


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        return request.user == user


class isAdm(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
