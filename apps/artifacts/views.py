from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artifact
from .serializers import ArtifactSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    parser_classes = (MultiPartParser, FormParser) # Critical for file uploads
    permission_classes = [permissions.IsAuthenticated] # Default
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'era']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def get_permissions(self):
        if self.action in ['explore', 'retrieve']:
             return [permissions.AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        # Default queryset relies on permissions, but we can restrict generic list
        return Artifact.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """Retrieve all artifacts owned by the authenticated user."""
        queryset = self.filter_queryset(Artifact.objects.filter(owner=request.user))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='type', description='Filter by media type', required=False, type=str),
            OpenApiParameter(name='era', description='Filter by era', required=False, type=str),
        ]
    )
    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def explore(self, request):
        """Public browsing of approved artifacts."""
        queryset = Artifact.objects.filter(status=Artifact.Status.APPROVED)
        queryset = self.filter_queryset(queryset) # Applies Search/Era/Type filters
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
