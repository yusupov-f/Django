from django.db import models


class Event(models.Model):
    # Ваши исходные поля
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()

    # Новые поля
    slug = models.SlugField(max_length=220, unique=True)
    summary = models.CharField(max_length=240)
    poster = models.ImageField(upload_to="events/posters/", blank=True)
    starts_at = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=220, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title