from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    """
    Represents an event that users can create and attend.

    Attributes:
        title (CharField): The name of the event (must be unique)
        slug (SlugField): URL-friendly version of the title
        excerpt (TextField): Short summary of the event (optional)
        description (TextField): Full details about the event
        featured_image (CloudinaryField): Main image for the event (optional)
        date (DateTimeField): When the event will occur
        location (CharField): Where the event will take place (optional)
        creator (ForeignKey): User who created the event
        created_on (DateTimeField): When the event was created (auto-set)
        attendees (ManyToManyField): Users attending through Attendance model

    Methods:
        save(): Auto-generates slug from title before saving
        __str__(): Human-readable representation
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_events")
    created_on = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(
        User,
        through='Attendance',
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
    """
    Represents a user's comment on an event.

    Attributes:
        event (ForeignKey): The event being commented on
        author (ForeignKey): User who wrote the comment
        body (TextField): The comment text content
        created_on (DateTimeField): When comment was made (auto-set)
        approved (BooleanField): Moderator approval status
        edited (BooleanField): Whether comment has been edited

    Meta:
        ordering: Comments sorted by creation date (oldest first)

    Methods:
        __str__(): Human-readable representation
    """
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Attendance(models.Model):
    """
    Tracks a user's attendance status for an event (through model).

    Attributes:
        STATUS_CHOICES: Possible attendance states
        user (ForeignKey): The attending user
        event (ForeignKey): The event being attended
        status (CharField): Attendance state from STATUS_CHOICES
        updated_on (DateTimeField): Last status update (auto-set)

    Meta:
        unique_together: Ensures one record per user-event pair

    Methods:
        __str__(): Human-readable representation
    """
    STATUS_CHOICES = [
        ('ATTENDING', 'Attending'),
        ('MAYBE', 'Maybe Attending'),
        ('NOT_ATTENDING', 'Not Attending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_ATTENDING'
    )
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.status})"
