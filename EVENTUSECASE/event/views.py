from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from event.forms import EventForm

from event.models import Event

class EventList(ListView):
    model = Event

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event:event_list')

class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event:event_list')

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event:event_list')
