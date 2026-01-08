from django.db import models
from django.conf import settings

class Artifact(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    class MediaType(models.TextChoices):
        IMAGE = 'image', 'Image'
        VIDEO = 'video', 'Video'
        AUDIO = 'audio', 'Audio'
        TEXT = 'text', 'Text'

    title = models.CharField(max_length=255)
    description = models.TextField()
    era = models.CharField(max_length=50, help_text="e.g. 1990s")
    type = models.CharField(max_length=20, choices=MediaType.choices)
    
    # File handling relying on Django storage abstraction
    file = models.FileField(upload_to='artifacts/%Y/%m/%d/')
    
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.PENDING
    )
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='artifacts'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
