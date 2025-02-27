from celery import shared_task

from habit_tracker.models import Habit
from habit_tracker.services import send_telegram_message


@shared_task
def habit_reminder():
    """
    Отправляет пользователю напоминание о начале выполнения привычки в Telegram.
    """
    message = "Сегодня хороший день, чтобы меняться!"
    habits = Habit.objects.filter(owner__isnull=False)

    for habit in habits:
        if habit.owner.tg_chat_id:
            send_telegram_message(habit.owner.tg_chat_id, message)
