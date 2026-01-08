from django.urls import path
from .views import ReviewQueueView, ApproveArtifactView, RejectArtifactView

urlpatterns = [
    path('queue', ReviewQueueView.as_view(), name='review-queue'),
    path('<int:artifactId>/approve', ApproveArtifactView.as_view(), name='approve-artifact'),
    path('<int:artifactId>/reject', RejectArtifactView.as_view(), name='reject-artifact'),
]
