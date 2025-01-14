from django.db import models

# Create your models here.
# Task(models.Model)
# title, description, created_at, status
STATUS = (
    ('tugallangan', 'Tugallangan'),
    ('tugallanmagan', 'Tugallanmagan'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default='tugallanmagan')

    def __str__(self):
        return self.title
    