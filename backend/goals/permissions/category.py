from rest_framework import permissions
from goals.models import GoalCategory, BoardParticipant


class GoalCategoryPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: GoalCategory):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user_id=request.user.id, board_id=obj.board.id).exists()
        return BoardParticipant.objects.filter(
            user_id=request.user.id,
            board_id=obj.board.id,
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer]
        ).exists()
