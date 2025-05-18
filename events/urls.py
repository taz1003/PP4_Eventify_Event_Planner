from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('accounts/', include('allauth.urls')),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/comment/edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/comment/delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
