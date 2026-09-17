from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу этого приложения
    path('', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_detail, name='event_detail')
]