from django.shortcuts import get_object_or_404, render
from .models import Event


def event_list(request):
    events = Event.objects.filter(is_published=True).order_by('-starts_at')
    return render(request, 'events/index.html', {'events': events})


def event_detail(request, pk):
    # Получаем событие по ID (pk)
    event = get_object_or_404(Event, pk=pk, is_published=True)
    return render(request, 'events/event_detail.html', {'event': event})