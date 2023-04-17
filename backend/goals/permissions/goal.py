from rest_framework import permissions
from goals.models import Goal, BoardParticipant


class GoalPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Goal):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user_id=request.user.id, board_id=obj.category.board).exists()
        return BoardParticipant.objects.filter(
            user_id=request.user.id,
            board_id=obj.category.board.id,
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer]
        ).exists()
