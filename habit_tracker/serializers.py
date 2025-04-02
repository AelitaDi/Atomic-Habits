from rest_framework import serializers

from habit_tracker.models import Habit
from habit_tracker.validators import (
    PeriodicValidator,
    DurationValidator,
    PleasantOrUsefulHabitValidator,
    RelatedPleasantHabitValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычек.
    """

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            PeriodicValidator("periodic"),
            DurationValidator("duration"),
            PleasantOrUsefulHabitValidator("is_pleasant", "related_to", "award"),
            RelatedPleasantHabitValidator("related_to"),
        ]
