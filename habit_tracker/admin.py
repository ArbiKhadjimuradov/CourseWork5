from habit_tracker.models import Habit
from django.contrib import admin


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "habit",
        "action",
        "pleasant_habit",
        "related_habit",
        "award",
        "publicity",
    )
    list_filter = ("publicity",)
    search_fields = ("habit",)
