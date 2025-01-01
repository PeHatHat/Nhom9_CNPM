from rest_framework import permissions

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers to access.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'MANAGER'

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['STAFF', 'MANAGER']

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or (request.user and request.user.role == 'ADMIN')
    
class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra xem user có phải là owner của object hay không
        return obj.owner == request.user or request.user.role in ['STAFF', 'MANAGER']
    
class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MEMBER'