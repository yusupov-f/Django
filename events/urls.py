from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    # Пустая строка '' означает главную страницу этого приложения
    path('', views.event_list, name='event_list'),
    # ИЗМЕНЕНО: Добавлен маршрут для создания события
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('<int:pk>/edit/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
]