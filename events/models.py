from django.db import models
from django.urls import reverse

# Менеджер, который возвращает только НЕ удаленные события
class ActiveEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


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
    
    # 1. Добавляем флаг мягкого удаления
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено (Soft Delete)')

    # 2. Подключаем менеджеры
    objects = ActiveEventManager()      # Event.objects.all() вернет ТОЛЬКО активные!
    all_objects = models.Manager()      # Event.all_objects.all() вернет ВСЕ (включая soft-deleted)

    def __str__(self):
        return self.title

    # Метод для удобного получения URL карточки
    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.pk})

    # 3. Переопределяем метод удаления
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()