from typing import Any
from rest_framework import serializers, exceptions
from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    verification_code = serializers.CharField(write_only=True)
    tg_id = serializers.SlugField(source='chat_id', read_only=True)

    class Meta:
        model = TgUser
        read_only_fields = ('tg_id', 'username', 'user_id')
        fields = ('tg_id', 'username', 'user_id', 'verification_code')

    def validate(self, attrs: dict[str, Any]):
        verification_code = attrs.get('verification_code')
        tg_user = TgUser.objects.filter(verification_code=verification_code).first()
        if not tg_user:
            raise exceptions.ValidationError({'verification_code': 'field is incorrect'})
        attrs['tg_user'] = tg_user
        return attrs
