# calculator/models.py
# Ma'lumotlar bazasi modellari - 4-kishi (Bobur) yozadi

from django.db import models
from django.contrib.auth.models import User


class CalculationHistory(models.Model):
    """
    Foydalanuvchining hisoblash tarixini saqlaydi.
    Har bir hisoblash bir qator sifatida saqlanadi.
    """

    # Qaysi foydalanuvchiga tegishli (user o'chirilsa, tarixi ham o'chadi)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # User o'chsa, uning tarixi ham o'chadi
        related_name='calculations',
        verbose_name='Foydalanuvchi'
    )

    # Misol: "log(100)" yoki "2 + 3"
    expression = models.CharField(
        max_length=500,
        verbose_name='Ifoda'
    )

    # Natija: "2.0" yoki "5"
    result = models.CharField(
        max_length=200,
        verbose_name='Natija'
    )

    # Qaysi tur: 'basic' = oddiy, 'advanced' = oliy matematika
    calculation_type = models.CharField(
        max_length=20,
        choices=[
            ('basic', 'Oddiy'),
            ('advanced', 'Oliy matematika'),
        ],
        default='basic',
        verbose_name='Tur'
    )

    # Qachon hisoblangan (avtomatik to'ldiriladi)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Vaqt'
    )

    class Meta:
        # Yangi hisoblashlar birinchi ko'rinadi
        ordering = ['-created_at']
        verbose_name = 'Hisoblash'
        verbose_name_plural = 'Hisoblashlar'

    def __str__(self):
        return f"{self.user.username}: {self.expression} = {self.result}"
