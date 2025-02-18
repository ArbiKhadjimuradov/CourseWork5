from rest_framework.viewsets import ModelViewSet
from habit_tracker.models import Habit
from habit_tracker.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """Вьюсет для модели Привычка."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
