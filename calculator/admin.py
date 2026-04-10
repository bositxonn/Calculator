# calculator/admin.py
# Admin panelda modellarni ko'rsatish - 4-kishi (Bobur) yozadi

from django.contrib import admin
from .models import CalculationHistory


@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    # Admin panelda qaysi ustunlar ko'rinsin
    list_display = ['user', 'expression', 'result', 'calculation_type', 'created_at']

    # Filtrlash paneli (o'ng tomonda)
    list_filter = ['calculation_type', 'created_at', 'user']

    # Qidiruv
    search_fields = ['user__username', 'expression', 'result']

    # Yangilardan eskiga tartib
    ordering = ['-created_at']

    # Faqat o'qish (tahrirlash kerak emas)
    readonly_fields = ['created_at']
