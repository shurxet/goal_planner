from django.db import models
from goals.models import BaseModel, Goal
from core.models import User


class GoalComment(BaseModel):
    goal = models.ForeignKey(Goal, verbose_name='Цель', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='comments')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
