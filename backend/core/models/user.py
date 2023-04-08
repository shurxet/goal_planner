from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(unique=True, null=True, blank=True, verbose_name="Номер телефона", help_text="Укажите номер телефона")
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Возраст", help_text="Укажите возрастcls")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        app_label = 'core'
        db_table = 'core_user'
