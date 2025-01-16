from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    