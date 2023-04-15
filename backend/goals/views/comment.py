from django.db.models import Q
from rest_framework import generics, filters
from goals.models import GoalComment
from goals import serializers
from goals.permissions import GoalCommentPermissions


class GoalCommentCreateView(generics.CreateAPIView):
    permission_classes = [GoalCommentPermissions]
    serializer_class = serializers.GoalCommentCreateSerializer


class GoalCommentListView(generics.ListAPIView):
    model = GoalComment
    permission_classes = [GoalCommentPermissions]
    serializer_class = serializers.GoalCommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-created']

    def get_queryset(self):
        query_params = self.request.GET['goal']
        return GoalComment.objects.prefetch_related('goal__category__board', 'user').filter(
            Q(goal__category__board__participants__user_id=self.request.user.id) & Q(goal_id=query_params)
        ).all()


class GoalCommentView(generics.RetrieveUpdateDestroyAPIView):
    model = GoalComment
    permission_classes = [GoalCommentPermissions]
    serializer_class = serializers.GoalCommentSerializer

    def get_queryset(self):
        return GoalComment.objects.prefetch_related('goal__category__board', 'user').filter(
            goal__category__board__participants__user_id=self.request.user.id
        )
