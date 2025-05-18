from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Event, Comment, Attendance
from django.contrib import messages
from .forms import CommentForm, EventForm


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

    attendance = None
    if request.user.is_authenticated:
        attendance = Attendance.objects.filter(user=request.user, event=event).first()

    attending_users = Attendance.objects.filter(event=event, status='ATTENDING').select_related('user')
    maybe_users = Attendance.objects.filter(event=event, status='MAYBE').select_related('user')
    not_attending_users = Attendance.objects.filter(event=event, status='NOT_ATTENDING').select_related('user')

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
            "attendance": attendance,
            "attending_users": attending_users,
            "maybe_users": maybe_users,
            "not_attending_users": not_attending_users,
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
            messages.success(request, 'Comment Deleted!')
        else:
            messages.error(request, 'You are not authorised to delete this comment')

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


@login_required
def update_attendance(request, slug, status):

    event = get_object_or_404(Event, slug=slug)

    if status not in ['ATTENDING', 'MAYBE', 'NOT_ATTENDING']:
        messages.error(request, "Invalid attendance status")
        return redirect('event_detail', slug=slug)

    attendance, created = Attendance.objects.get_or_create(user=request.user, event=event)
    attendance.status = status
    attendance.save()

    messages.success(request, f"You selected '{attendance.get_status_display()}'.")
    return redirect('event_detail', slug=slug)


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            messages.success(request, 'Event created successully')
            return redirect('event_detail', slug=event.slug)
    else:
        form = EventForm()

    return render(
        request,
        "events/event_form.html",
        {
            'form': form,
            'action': 'Create'
        }
    )


@login_required
def edit_event(request, slug):
    event = get_object_or_404(Event, slug=slug)

    if request.user != event.creator:
        messages.error(request, "You are not authorized to edit this event")
        return redirect('event_detail', slug=event.slug)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfuly")
            return redirect('event_detail', slug=event.slug)
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "events/event_form.html",
        {
            'form': form,
            'action': 'Edit'
        }
    )


@login_required
def delete_event(request, slug):
    event = get_object_or_404(Event, slug=slug)

    if request.user != event.creator:
        messages.error(request, "You are not authorized to delete this event")
        return redirect('event_detail', slug=event.slug)

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfuly")
        return redirect('event_list')

    messages.error(request, 'Invalid request')
    return redirect('event_detail', slug=slug)
