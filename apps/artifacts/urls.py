from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtifactViewSet

router = DefaultRouter()
router.register(r'', ArtifactViewSet, basename='artifacts')

urlpatterns = [
    path('', include(router.urls)),
]
