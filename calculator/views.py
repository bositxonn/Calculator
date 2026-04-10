# calculator/views.py
# Sahifalar va hisoblash mantiqi - 2-kishi (Jasur) yozadi

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import json

from .models import CalculationHistory
from .utils import calculate_basic, calculate_advanced


def home(request):
    """
    Bosh sahifa - oddiy kalkulyator.
    HAMMA ko'ra oladi, login shart emas.
    """
    history = []

    # Agar login bo'lgan bo'lsa, oxirgi 10 ta hisoblashni ko'rsat
    if request.user.is_authenticated:
        history = CalculationHistory.objects.filter(
            user=request.user
        ).order_by('-created_at')[:10]

    return render(request, 'calculator/home.html', {
        'history': history,
    })


def basic_calculate(request):
    """
    Oddiy hisoblash API - POST so'rov qabul qiladi.
    URL: /calculate/basic/
    Login shart emas.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Faqat POST!'}, status=405)

    try:
        data = json.loads(request.body)
        expression = data.get('expression', '').strip()
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Noto\'g\'ri JSON!'}, status=400)

    if not expression:
        return JsonResponse({'error': 'Ifoda bo\'sh!'}, status=400)

    result, error = calculate_basic(expression)

    if error:
        return JsonResponse({'error': error}, status=400)

    # Agar login bo'lgan bo'lsa, tarixga saqlash
    if request.user.is_authenticated:
        CalculationHistory.objects.create(
            user=request.user,
            expression=expression,
            result=result,
            calculation_type='basic'
        )

    return JsonResponse({
        'result': result,
        'expression': expression
    })


@login_required  # ← BU MUHIM! Login bo'lmasa /accounts/login/ ga yuboradi
def advanced_view(request):
    """
    Oliy matematika sahifasi.
    FAQAT login bo'lgan foydalanuvchilar kirishi mumkin!
    """
    history = CalculationHistory.objects.filter(
        user=request.user,
        calculation_type='advanced'
    ).order_by('-created_at')[:10]

    return render(request, 'calculator/advanced.html', {
        'history': history,
    })


@login_required  # ← Bu ham login talab qiladi
def advanced_calculate(request):
    """
    Oliy matematika hisoblash API.
    URL: /calculate/advanced/
    FAQAT login bo'lgan foydalanuvchilar uchun!
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Faqat POST!'}, status=405)

    try:
        data = json.loads(request.body)
        func_name = data.get('function', '')
        value = data.get('value', 0)
        base = data.get('base', None)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Noto\'g\'ri JSON!'}, status=400)

    result, expr_or_error = calculate_advanced(func_name, value, base)

    if result is None:
        return JsonResponse({'error': expr_or_error}, status=400)

    # Tarixga saqlash
    CalculationHistory.objects.create(
        user=request.user,
        expression=expr_or_error,  # calculate_advanced ifodani qaytaradi
        result=result,
        calculation_type='advanced'
    )

    return JsonResponse({
        'result': result,
        'expression': expr_or_error
    })


@login_required
def history_view(request):
    """
    Barcha hisoblashlar tarixi.
    URL: /history/
    Faqat login bo'lgan foydalanuvchilarga ko'rinadi.
    """
    all_history = CalculationHistory.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'calculator/history.html', {
        'history': all_history,
    })


@login_required
def clear_history(request):
    """
    Tarixni tozalash.
    URL: /history/clear/
    """
    if request.method == 'POST':
        CalculationHistory.objects.filter(user=request.user).delete()
        messages.success(request, 'Tarix muvaffaqiyatli tozalandi!')
    return redirect('history')
