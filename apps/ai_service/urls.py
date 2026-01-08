from django.urls import path
from .views import GenerateBackstoryView

urlpatterns = [
    path('generate-backstory', GenerateBackstoryView.as_view(), name='generate-backstory'),
]
