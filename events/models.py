from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(
        max_length=220, unique=True, blank=True, verbose_name='URL (Slug)'
    )
    summary = models.CharField(
        max_length=240, blank=True, verbose_name='Краткое описание'
    )
    description = models.TextField(verbose_name='Полное описание')
    poster = models.ImageField(
        upload_to='events/posters/', blank=True, verbose_name='Постер'
    )
    starts_at = models.DateTimeField(verbose_name='Дата и время проведения')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title