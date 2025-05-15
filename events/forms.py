from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    model = Comment
    fields = ('body',)
    widgets = {
        'body': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Add your comment here...'
        }),
    }
