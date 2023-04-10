from django.db import models
from goals.models import GoalCategory, BaseModel
from core.models import User


class Goal(BaseModel):
    class Status(models.IntegerChoices):
        to_do = 1, 'К выполнению'
        in_progress = 2, 'В процессе'
        done = 3, 'Выполнено'
        archived = 4, 'Архив'

    class Priority(models.IntegerChoices):
        low = 1, 'Низкий'
        medium = 2, 'Средний'
        high = 3, 'Высокий'
        critical = 4, 'Критический'

    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='goals')
    category = models.ForeignKey(GoalCategory, verbose_name='Категория', on_delete=models.PROTECT, related_name='goals')
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=Status.choices, default=Status.to_do)
    priority = \
        models.PositiveSmallIntegerField(verbose_name='Приоритет', choices=Priority.choices, default=Priority.medium)
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата выполнения')

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.title
