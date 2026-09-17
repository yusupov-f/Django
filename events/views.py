from django.shortcuts import get_object_or_404, render
from .models import Event


def event_list(request):
    events = Event.objects.filter(is_published=True).order_by('-starts_at')
    # Используем созданный event_list.html
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True)
    # Используем детальный шаблон event_detail.html
    return render(request, 'events/event_detail.html', {'event': event})