from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=100)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_events")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
