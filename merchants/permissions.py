from rest_framework import permissions


class IsUserNotBlocked(permissions.BasePermission):
    message = 'Пользователь заблокирован администратором системы.'

    def has_permission(self, request, view):
        return bool(request.user and not request.user.blocked)
