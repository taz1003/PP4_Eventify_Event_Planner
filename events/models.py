from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', blank=True, null=True)
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

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


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('ATTENDING', 'Attending'),
        ('MAYBE', 'Maybe Attending'),
        ('NOT_ATTENDING', 'Not Attending'),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='NOT_ATTENDING')
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # one status per user per event

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.status})"
