from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", help_text="Загрузите ваш аватар", **NULLABLE
    )

    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        **NULLABLE,
    )

    tg_nik = models.CharField(max_length=50, verbose_name="TG", help_text="Укажите TG ник", **NULLABLE)

    tg_chat_id = models.CharField(max_length=50, verbose_name="TG chat_id", help_text="Укажите TG chat_id", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ["email"]

    def __str__(self):
        return self.email
