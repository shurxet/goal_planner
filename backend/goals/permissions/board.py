from rest_framework import permissions
from goals.models import Board, BoardParticipant


class BoardPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Board):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user_id=request.user.id, board_id=obj.id).exists()
        return BoardParticipant.objects.filter(
            user_id=request.user.id, board_id=obj.id, role=BoardParticipant.Role.owner
        ).exists()
