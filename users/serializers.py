from rest_framework.serializers import ModelSerializer

from habit_tracker.serializers import HabitSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для просмотра общей информации о пользователях.
    """

    habits = HabitSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ("email", "is_active", "is_staff", "id", "habits")


class UserSelfSerializer(ModelSerializer):
    """
    Сериализатор для создания, редактирования и просмотра собственного профиля.
    """

    class Meta:
        model = User
        fields = "__all__"
