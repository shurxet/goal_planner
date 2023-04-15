from django.db import models
from goals.models import BaseModel
from core.models import User


class Board(BaseModel):
    title = models.CharField(verbose_name='Название', max_length=255)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'


class BoardParticipant(BaseModel):
    class Role(models.IntegerChoices):
        owner = 1, 'Владелец'
        writer = 2, 'Редактор'
        reader = 3, 'Читатель'

    board = models.ForeignKey(Board, verbose_name='Доска', on_delete=models.PROTECT, related_name='participants')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, related_name='participants')
    role = models.PositiveSmallIntegerField(verbose_name='Роль', choices=Role.choices, default=Role.owner)

    class Meta:
        unique_together = ('board', 'user')
        verbose_name = 'частник'
        verbose_name_plural = 'Участники'
