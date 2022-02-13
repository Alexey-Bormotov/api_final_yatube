from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):

        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)
