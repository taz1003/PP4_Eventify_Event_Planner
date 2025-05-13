from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('accounts/', include('allauth.urls')),
]
