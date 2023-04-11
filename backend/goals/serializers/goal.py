from typing import Type
from rest_framework import serializers
from goals.models import GoalCategory, Goal
from rest_framework.exceptions import PermissionDenied


class GoalCreateSerializer(serializers.ModelSerializer):
    category =\
        serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.filter(is_deleted=False),label='Категория')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value: Type[GoalCategory]):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')
        if value.user != self.context['request'].user:
            raise PermissionDenied
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
            raise PermissionDenied
        return value
