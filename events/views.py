from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from .models import Event, Comment
from django.contrib import messages

# Create your views here.


class EventList(ListView):
    model = Event
    template_name = "events/index.html"
    context_object_name = 'events'
    paginate_by = 6


# class event_detail(request, slug):
#     event = get_object_or_404(Event, slug=slug)
#     comments = event.comments.filter(approved=True).order_by('-created_on')
#     comment_count = comments.count()
