from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
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
    comments = event.comments.all().order_by("-created_on")
    comment_count = comments.filter(approved=True).count()
    user_attendance = None

    if request.user.is_authenticated:
        user_attendance = Attendance.objects.filter(user=request.user, event=event).first()

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
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_attendance": user_attendance,
        },
    )


def comment_edit(request, slug, comment_id):

    event = get_object_or_404(Event, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, "You are not authorized to edit this comment")
        return redirect('event_detail', slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.approved = False
            comment.edited = True
            comment.save()
            messages.success(request, 'Comment Updated!')
            return redirect('event_detail', slug=slug)
    else:
        comment_form = CommentForm(instance=comment)

    return render(request,
                  "events/comment_edit.html", {
                      "comment_form": comment_form,
                      "event": event,
                      "comment": comment,
                  })


def comment_delete(request, slug, comment_id):

        event = get_object_or_404(Event, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user:
            comment.delete()
            messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))
