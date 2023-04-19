from rest_framework import generics, permissions, response
from bot.models import TgUser
from bot import serializers
from bot.tg import TgClient
from backend import settings


class UserVerificationView(generics.GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TgUserSerializer

    def patch(self, request, *args, **kwargs):
        s: serializers.TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data['tg_user']
        tg_user.user = self.request.user
        tg_user.save(update_fields=('user',))

        instance_s: serializers.TgUserSerializer = self.get_serializer(tg_user)
        TgClient(settings.BOT_TOKEN).send_message(tg_user.chat_id, '[verification_has_been_completed]')
        return response.Response(instance_s.data)
