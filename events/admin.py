from django.contrib import admin
from .models import Event, Comment, Attendance
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventsAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing Events with Summernote rich text editing.
    Configures display, filtering, search, and auto-slug generation.
    """

    list_display = ('title', 'creator', 'date', 'location', 'created_on')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing Comments with approval functionality.
    Includes bulk approval action and filters for moderation workflow.
    """

    list_display = ('author', 'event', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Attendance)
class AttendanceAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing Attendance records.
    Allows direct editing of status and provides date-based navigation.
    """

    list_display = ('user', 'event', 'status', 'updated_on')
    list_filter = ('status', 'updated_on')
    search_fields = ('user__username', 'event__title')
    date_hierarchy = 'updated_on'
    list_editable = ('status',)
