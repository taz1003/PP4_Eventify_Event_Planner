from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Event)
# class EventsAdmin(SummernoteModelAdmin):

#     list_display = ('title', 'status')
#     search_fields = ['title']
#     list_filter = ('status',)
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)

# Register your models here.

admin.site.register(Event)
admin.site.register(Comment)
