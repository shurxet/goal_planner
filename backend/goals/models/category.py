from django.db import models
from goals.models import BaseModel
from core.models import User
from goals.models.board import Board


class GoalCategory(BaseModel):
    board = models.ForeignKey(Board, verbose_name="Доска", on_delete=models.PROTECT, related_name="categories")
    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='categories')
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
