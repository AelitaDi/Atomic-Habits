from rest_framework import serializers


class PeriodicValidator:
    """
    Валидатор проверки периодичности привычки (не реже 1 раза в неделю и не чаще 7ми раз в неделю).
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodic = value.get(self.field)
        if not 1 <= periodic <= 7:
            raise serializers.ValidationError(
                "Периодичность привычки не должна быть реже, чем 1 раз в неделю и не чаще, чем 7 раз в неделю"
            )


class DurationValidator:
    """
    Валидатор проверки длительности выполнения привычки не более 120 сек.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get(self.field)
        if time and time.total_seconds > 120:
            raise serializers.ValidationError("Время выполнения привычки должно быть не более 120 секунд")


class PleasantOrUsefulHabitValidator:
    """
    Валидатор проверки наличия у приятной привычки связанной привычки или вознаграждения.
    """

    def __init__(self, is_pleasant, related_to, award):
        self.is_pleasant = is_pleasant
        self.related_to = related_to
        self.award = award

    def __call__(self, value):
        is_pleasant_field = value.get(self.is_pleasant)
        related_to_field = value.get(self.related_to)
        award_field = value.get(self.award)

        if is_pleasant_field:
            if related_to_field or award_field:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения."
                )
        else:
            if related_to_field and award_field:
                raise serializers.ValidationError(
                    "У полезной привычки не может быть одновременно вознаграждения и связанной привычки."
                )


class RelatedPleasantHabitValidator:
    """
    Валидатор проверки связанной привычки на признак приятной привычки.
    """

    def __init__(self, related_to):
        self.related_to = related_to

    def __call__(self, value):
        habit = value.get(self.related_to)

        if habit:
            if not habit.is_pleasant:
                raise serializers.ValidationError("Связанная привычка должна иметь признак приятной привычки.")
