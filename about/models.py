from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Model representing the 'About' page content.
    Attributes:
    Stores 'About' page content with title, content, image, and metadata.
    Auto-updates timestamp when modified.

    Methods:
        __str__: Returns the title of the about page for display purposes.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
