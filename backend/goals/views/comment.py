from django.db.models import Q
from rest_framework import generics, permissions, filters
from goals.models import GoalComment
from goals import serializers


class GoalCommentCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentCreateSerializer


class GoalCommentListView(generics.ListAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['goal']
    ordering = ['-created']

    def get_queryset(self):
        query_params = self.request.GET['goal']
        return GoalComment.objects.filter(Q(user_id=self.request.user.id) & Q(goal_id=query_params)).all()


class GoalCommentView(generics.RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalComment.objects.filter(user_id=self.request.user.id)
