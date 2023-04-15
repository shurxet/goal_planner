from rest_framework import permissions
from goals.models import GoalComment, BoardParticipant


class GoalCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: GoalComment):
        if not request.user.is_authenticated:
            return False
        return any((request.method in permissions.SAFE_METHODS, obj.user_id == request.user.id))
