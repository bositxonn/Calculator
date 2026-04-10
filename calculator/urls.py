# calculator/urls.py
# Kalkulyator ilovasining URL yo'nalishlari

from django.urls import path
from . import views

urlpatterns = [
    # Bosh sahifa - oddiy kalkulyator
    path('', views.home, name='home'),

    # Oddiy hisoblash API (AJAX uchun)
    path('calculate/basic/', views.basic_calculate, name='basic_calculate'),

    # Oliy matematika sahifasi (login kerak!)
    path('advanced/', views.advanced_view, name='advanced'),

    # Oliy matematika hisoblash API (login kerak!)
    path('calculate/advanced/', views.advanced_calculate, name='advanced_calculate'),

    # Hisoblashlar tarixi (login kerak!)
    path('history/', views.history_view, name='history'),

    # Tarixni tozalash (login kerak!)
    path('history/clear/', views.clear_history, name='clear_history'),
]
