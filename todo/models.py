from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    related_date = models.DateField(null=True)
    created_by = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('related_date','-created_at',)

    def __str__(self):
        return self.title
