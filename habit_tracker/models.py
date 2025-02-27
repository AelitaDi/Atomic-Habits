from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """
    Модель привычки.
    """

    place = models.CharField(
        max_length=150, verbose_name="Место", help_text="Укажите место, где будете выполнять привычку"
    )
    time = models.TimeField(
        default="00:00", verbose_name="Время", help_text="Укажите время, в которое будете выполнять привычку"
    )
    action = models.CharField(max_length=150, verbose_name="Действие", help_text="Укажите действие")
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак полезной привычки",
        help_text="Поставьте галочку, если это приятная привычка",
    )
    related_to = models.ForeignKey(
        "Habit",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        related_name="related_habit",
        **NULLABLE,
    )
    periodic = models.IntegerField(
        default=1, verbose_name="Периодичность", help_text="Укажите, сколько раз в неделю вы будете выполнять привычку"
    )
    award = models.CharField(
        max_length=250, verbose_name="Вознаграждение", help_text="Укажите, чем вы себя вознаградите", **NULLABLE
    )
    duration = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Длительность",
        help_text="Укажите длительность выполнения привычки",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Поставьте галочку, если хотите, чтобы эту привычку видели все",
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        related_name="habits",
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place} {self.periodic} раз в неделю."

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
