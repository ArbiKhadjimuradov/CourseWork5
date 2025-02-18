from rest_framework.routers import SimpleRouter
from habit_tracker.views import HabitViewSet
from habit_tracker.apps import HabitConfig

app_name = HabitConfig.name
router = SimpleRouter()
router.register("", HabitViewSet)
urlpatterns = []
urlpatterns += router.urls
