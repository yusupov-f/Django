from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event
        fields = [
            'title','slug','summary','description','starts_at','is_published',]

        widgets = {
            'starts_at': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
        }