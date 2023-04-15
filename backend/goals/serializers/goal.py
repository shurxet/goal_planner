from typing import Type
from rest_framework import serializers, exceptions
from goals.models import GoalCategory, Goal, BoardParticipant


class GoalCreateSerializer(serializers.ModelSerializer):
    category =\
        serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.filter(is_deleted=False), label='Категория')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value: GoalCategory):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')
        if value.user != self.context['request'].user:
            raise exceptions.PermissionDenied
        if not BoardParticipant.objects.filter(
                board_id=value.board_id,
                role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
                user=self.context['request'].user
        ).exists():
            raise serializers.ValidationError('You must be owner or writer')
        return value

class GoalSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=GoalCategory.objects.filter(is_deleted=False)
    )

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value: Type[GoalCategory]):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')
        if value.user != self.context['request'].user:
            raise exceptions.PermissionDenied
        return value
