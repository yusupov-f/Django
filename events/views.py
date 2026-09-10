from django.shortcuts import render

from events.models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

