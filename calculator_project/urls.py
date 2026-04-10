# calculator_project/urls.py
# Loyihaning asosiy URL yo'naltiruvchisi

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel: http://localhost:8000/admin/
    path('admin/', admin.site.urls),

    # Kalkulyator sahifalari: http://localhost:8000/
    path('', include('calculator.urls')),

    # Auth sahifalari: http://localhost:8000/accounts/
    path('accounts/', include('accounts.urls')),
]
