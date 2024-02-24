from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class IsAdminOrReadAndPatch(permissions.BasePermission):

    def has_permission(self, request, view):

        print('request', request._auth)
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'PATCH' and request._auth is not None:
            return True
        return bool(request.user and request.user.is_staff)