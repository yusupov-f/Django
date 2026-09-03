from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу этого приложения
    path('', views.hi, name='home'),
]