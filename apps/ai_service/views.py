from rest_framework import views, status, response, serializers
from drf_spectacular.utils import extend_schema
from .services import ai_generator

class GenerateBackstoryRequestSerializer(serializers.Serializer):
    descriptions = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,
        help_text="List of artifact descriptions to generate a backstory from."
    )

class GenerateBackstoryResponseSerializer(serializers.Serializer):
    backstory = serializers.CharField()

class GenerateBackstoryView(views.APIView):
    """
    Generate a shared narrative from multiple artifact descriptions.
    """
    serializer_class = GenerateBackstoryRequestSerializer

    @extend_schema(
        request=GenerateBackstoryRequestSerializer,
        responses={200: GenerateBackstoryResponseSerializer}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        descriptions = serializer.validated_data['descriptions']
        backstory = ai_generator.generate(descriptions)
        
        return response.Response({"backstory": backstory}, status=status.HTTP_200_OK)
