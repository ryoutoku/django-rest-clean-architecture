from rest_framework import routers
from .views import QuestionViewSet, ChoiceViewSet


router = routers.SimpleRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
urlpatterns = router.urls
