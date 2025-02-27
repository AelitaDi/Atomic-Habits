from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test_user@example.com")
        self.habit = Habit.objects.create(
            place="дома", time="07:00:00", action="съесть овсянку", periodic=2, award="съесть яблоко", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """
        Тест на получение данных привычки.
        """
        url = reverse("habit_tracker:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        """
        Тест на создание привычки.
        """
        url = reverse("habit_tracker:habit_create")
        data = {
            "place": "школа",
            "time": "07:00:00",
            "action": "причесаться",
            "periodic": 5,
            "award": "улыбнуться себе в зеркало",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_delete(self):
        """
        Тест на удаление привычки.
        """
        url = reverse("habit_tracker:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """
        Тест на получение списка привычек.
        """
        url = reverse("habit_tracker:habits_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "is_pleasant": self.habit.is_pleasant,
                    "periodic": self.habit.periodic,
                    "award": self.habit.award,
                    "duration": "00:02:00",
                    "is_public": self.habit.is_public,
                    "related_to": self.habit.related_to,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"DATA:    {data}")
        print(f"RESULT:  {result}")
        self.assertEqual(data, result)
