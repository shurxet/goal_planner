from rest_framework import serializers
from goals.models import GoalCategory, Board , BoardParticipant
from core.serializers import UserProfileSerializer


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated', 'user', 'is_deleted')
        fields = '__all__'

    def validate_board(self, value: Board):
        if value.is_deleted:
            raise serializers.ValidationError('Not allowed to delete category')

        if not BoardParticipant.objects.filter(
            board=value,
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            user=self.context['request'].user
        ).exists():
            raise serializers.ValidationError('You must be owner or writer')
        return value


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated', 'user', 'board')
        fields = '__all__'
