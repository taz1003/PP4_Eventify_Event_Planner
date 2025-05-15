from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'creator', 'date', 'location', 'created_on')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('author', 'event', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
