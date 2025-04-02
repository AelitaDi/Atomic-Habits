from django.urls import path
from habit_tracker.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

from habit_tracker.apps import HabitTrackerConfig

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
