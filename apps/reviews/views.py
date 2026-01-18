from rest_framework import generics, views, status, response
from apps.artifacts.models import Artifact
from apps.artifacts.serializers import ArtifactSerializer
from .permissions import IsReviewer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

class ReviewQueueView(generics.ListAPIView):
    queryset = Artifact.objects.filter(status=Artifact.Status.PENDING)
    serializer_class = ArtifactSerializer
    permission_classes = [IsAuthenticated,IsReviewer]

class ApproveArtifactView(views.APIView):
    permission_classes = [IsReviewer]

    @extend_schema(responses={200: "Approved"})
    def post(self, request, artifactId):
        try:
            artifact = Artifact.objects.get(id=artifactId)
            artifact.status = Artifact.Status.APPROVED
            artifact.save()
            return response.Response({"status": "approved"}, status=status.HTTP_200_OK)
        except Artifact.DoesNotExist:
            return response.Response({"error": "Artifact not found"}, status=status.HTTP_404_NOT_FOUND)

class RejectArtifactView(views.APIView):
    permission_classes = [IsReviewer]

    @extend_schema(responses={200: "Rejected"})
    def post(self, request, artifactId):
        try:
            artifact = Artifact.objects.get(id=artifactId)
            artifact.status = Artifact.Status.REJECTED
            artifact.save()
            return response.Response({"status": "rejected"}, status=status.HTTP_200_OK)
        except Artifact.DoesNotExist:
            return response.Response({"error": "Artifact not found"}, status=status.HTTP_404_NOT_FOUND)
