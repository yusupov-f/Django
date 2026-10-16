from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Event


def event_list(request):
    # Показываем только опубликованные и НЕ удаленные квесты
    events = Event.objects.filter(is_published=True, is_deleted=False).order_by('-starts_at')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    # Не даем открыть детальную страницу, если квест удален
    event = get_object_or_404(Event, pk=pk, is_published=True, is_deleted=False)
    return render(request, 'events/event_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(
                request, f'Событие "{event.title}" успешно создано!'
            )
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm()

    return render(
        request,
        'events/event_form.html',
        {'form': form, 'action': 'Создать событие'},
    )


def event_update(request, pk):
    # Не даем редактировать удаленный квест
    event = get_object_or_404(Event, pk=pk, is_deleted=False)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            messages.success(
                request, f'Событие "{event.title}" успешно обновлено!'
            )
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)

    return render(
        request,
        'events/event_form.html',
        {'form': form, 'action': 'Редактировать событие'},
    )


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, is_deleted=False)

    if request.method == 'POST':
        title = event.title
        # Вызов переопределенного метода models.py (ставит is_deleted = True)
        event.delete()
        messages.success(request, f'Событие "{title}" было успешно удалено.')
        return redirect('events:event_list')

    return redirect('events:event_detail', pk=pk)