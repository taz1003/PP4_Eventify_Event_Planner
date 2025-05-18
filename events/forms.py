from django import forms
from .models import Event, Comment
from django.utils import timezone


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments on events.

    Attributes:
        body (Textarea): The comment text input field with Bootstrap styling.
                        Configured with a placeholder and 3 visible rows.

    Meta:
        model: Comment - The model this form is associated with
        fields: ['body'] - Only includes the comment body field
        labels: Removes the default label for cleaner presentation
    """
    class Meta:
        model = Comment
        fields = ['body',]
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add your comment here...'
            }),
        }


class EventForm(forms.ModelForm):
    """
    Form for creating and updating event listings.

    Includes validation to ensure event dates are in the future.
    Uses a datetime-local input widget for better date/time selection.

    Fields:
        - title: Event name
        - excerpt: Short summary
        - description: Full details (Summernote rich text)
        - featured_image: Optional header image
        - date: Future datetime (validated)
        - location: Venue information

    Validation:
        clean_date(): Ensures event date isn't in the past
    """
    class Meta:
        model = Event
        fields = ['title', 'excerpt',
                  'description', 'featured_image',
                  'date', 'location']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        def clean_date(self):
            date = self.cleaned_data.get('date')
            if date and date < timezone.now():
                raise forms.ValidationError("Event date cannot be in the past")
            return date
