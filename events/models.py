from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default="a_slug", max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_events")
    created_on = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(
        User,
        related_name='attending_events',
        blank=True
    )

    def __str__(self):
        return f"Event: {self.title} created by {self.creator}"

    class Meta:
        ordering = ['date']


class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
