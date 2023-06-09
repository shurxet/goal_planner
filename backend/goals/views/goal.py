from typing import Type
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from goals.permissions import GoalPermissions
from goals.filters import GoalDateFilter
from goals.models.goal import Goal
from goals import serializers


class GoalCreateView(generics.CreateAPIView):
    permission_classes = [GoalPermissions]
    serializer_class = serializers.GoalCreateSerializer


class GoalListView(generics.ListAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = serializers.GoalSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = GoalDateFilter
    ordering = ['title']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Goal.objects.prefetch_related('user', 'category__board').filter(
            Q(category__board__participants__user_id=self.request.user.id) & ~Q(status=Goal.Status.archived)
        )


class GoalView(generics.RetrieveUpdateDestroyAPIView):
    model = Goal
    permission_classes = [GoalPermissions]
    serializer_class = serializers.GoalSerializer

    def get_queryset(self):
        return Goal.objects.prefetch_related('user', 'category__board').filter(
            Q(category__board__participants__user_id=self.request.user.id) & ~Q(status=Goal.Status.archived)
        )

    def perform_destroy(self, instance: Type[Goal]):
        instance.status = Goal.Status.archived
        instance.save(update_fields=('status',))
        return instance
