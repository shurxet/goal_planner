from rest_framework import generics, filters, permissions
from django.db import transaction
from goals.permissions import BoardPermissions
from goals.models import Board, Goal
from goals import serializers


class BoardCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BoardCreateSerializer


class BoardListView(generics.ListAPIView):
    model = Board
    permission_classes = [BoardPermissions]
    serializer_class = serializers.BoardListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['title']

    def get_queryset(self):
        return Board.objects.prefetch_related('participants').filter(
            participants__user_id=self.request.user.id, is_deleted=False
        )


class BoardView(generics.RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [BoardPermissions]
    serializer_class = serializers.BoardSerializer

    def get_queryset(self):
        return Board.objects.prefetch_related('participants').filter(
            participants__user_id=self.request.user.id, is_deleted=False
        )

    def perform_destroy(self, instance: Board):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save(update_fields=('is_deleted',))
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(status=Goal.Status.archived)
        return instance
