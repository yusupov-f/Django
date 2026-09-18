from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EventForm
from .models import Event


def event_list(request):
    events = Event.objects.filter(is_published=True).order_by('-starts_at')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True)
    return render(request, 'events/event_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('events:event_list')
    else:   
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form, 'action': 'Создать'})