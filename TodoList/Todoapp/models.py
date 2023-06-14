from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.pk} - {self.text}"
    