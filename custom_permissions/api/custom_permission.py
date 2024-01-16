from rest_framework.permissions import BasePermission
from rest_framework.response import Response
class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=="POST":
            return True
        return False