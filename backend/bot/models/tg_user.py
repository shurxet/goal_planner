from django.db import models
from core.models import User


class TgUser(models.Model):
    chat_id = models.BigIntegerField(unique=True, verbose_name='Chat ID')
    username = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name='Имя пользователя')
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name='Пользователь')
    verification_code = models.CharField(max_length=100, null=True, blank=True, default=None)
