from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Event, Comment, Attendance
from django.contrib import messages
from .forms import CommentForm

# Create your views here.


class EventList(ListView):
    model = Event
    template_name = "events/index.html"
    context_object_name = 'events'
    paginate_by = 6


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = event.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

        comment_form = CommentForm()

        return render(
            request,
            "events/event_detail.html",
            {
                "event": event,
                "comments": comment,
                "comment_count": comment_count,
                "comment_form": comment_form
            },
        )
