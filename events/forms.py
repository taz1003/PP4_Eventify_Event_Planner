from django import forms
from .models import Event, Comment
from django.utils import timezone


class CommentForm(forms.ModelForm):
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
    class Meta:
        model = Event
        fields = ['title', 'excerpt', 'description', 'featured_image', 'date', 'location']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        def clean_date(self):
            date = self.cleaned_data.get('date')
            if date and date < timezone.now():
                raise forms.ValidationError("Event date cannot be in the past")
            return date
