from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'TECH'


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CLIENT'

class TicketAccessPermission(BasePermission):
    """
    ADMIN: acesso total
    TECH: apenas tickets atribuídos a ele
    CLIENT: apenas tickets do próprio cliente
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == 'ADMIN':
            return True

        if user.role == 'TECH':
            return obj.technician == user

        if user.role == 'CLIENT':
            return obj.client.user == user

        return False
