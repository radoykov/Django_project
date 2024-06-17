from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.author == request.user

class IsAdminOrReadOnly(permissions.IsAdminUser):  
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        isAdmin = super(IsAdminOrReadOnly, self).has_permission(request, view)
        return isAdmin