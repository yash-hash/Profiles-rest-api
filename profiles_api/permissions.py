from rest_framework import permissions

#permission class to user
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile only"""

    def has_object_permission(self, request, view, obj):
        """Check wether using is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
