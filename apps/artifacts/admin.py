from django.contrib import admin
from .models import Artifact

@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'era', 'status', 'owner', 'created_at')
    list_filter = ('status', 'type', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
