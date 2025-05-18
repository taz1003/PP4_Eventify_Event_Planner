from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('accounts/', include('allauth.urls')),
    path('create/', views.create_event, name='create_event'),
    path('profile/', views.profile_view, name='profile'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/edit/', views.edit_event, name='edit_event'),
    path('<slug:slug>/delete/', views.delete_event, name='delete_event'),
    path('<slug:slug>/comment/edit/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/comment/delete/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/attendance/<str:status>',
         views.update_attendance, name='update_attendance'),
]
