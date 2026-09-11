# from django.contrib import admin
# from .models import Event


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     # Поля, которые будут отображаться в списке всех событий
#     list_display = ('title', 'starts_at', 'is_published', 'created_at')

#     # Фильтры в правой колонке
#     list_filter = ('is_published', 'starts_at')

#     # Поиск по названию и описанию
#     search_fields = ('title', 'description')

#     # Автоматически генерирует slug из названия при вводе
#     prepopulated_fields = {'slug': ('title',)}



from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts_at', 'is_published', 'created_at')
    list_filter = ('is_published', 'starts_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, EventAdmin)