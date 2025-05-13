from django.views.generic import ListView
from django.utils import timezone
from .models import Event

# Create your views here.


class EventList(ListView):
    model = Event
    template_name = "events/index.html"
    context_object_name = 'events'
    paginate_by = 6
