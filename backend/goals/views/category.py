from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from goals.permissions import GoalCategoryPermissions
from goals.models import GoalCategory, Goal
from django.db import transaction
from goals import serializers


class GoalCategoryCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategoryCreateSerializer


class GoalCategoryListView(generics.ListAPIView):
    model = GoalCategory
    permission_classes = [GoalCategoryPermissions]
    serializer_class = serializers.GoalCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['board']
    ordering_fields = ['title', 'created']
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return GoalCategory.objects.prefetch_related('board__participants').filter(
            board__participants__user_id=self.request.user, is_deleted=False
        )


class GoalCategoryView(generics.RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    permission_classes = [GoalCategoryPermissions]
    serializer_class = serializers.GoalCategorySerializer

    def get_queryset(self):
        return GoalCategory.objects.prefetch_related('board__participants').filter(
            board__participants__user_id=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: GoalCategory):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save(update_fields=('is_deleted',))
            Goal.objects.filter(category=instance).update(status=Goal.Status.archived)
        return instance
