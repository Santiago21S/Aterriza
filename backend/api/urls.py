from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GuideViewSet, health

router = DefaultRouter()
router.register("guides", GuideViewSet, basename="guide")

urlpatterns = [
    path("health/", health, name="health"),
    path("", include(router.urls)),
]
