# accounts/views.py
# Login, logout, register sahifalari - 3-kishi (Dilshod) yozadi

import os
import json
import time
from google import genai
from google.genai import types

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .forms import RegisterForm, LoginForm
from .models import Profile, ChatMessage


def register_view(request):
    """
    Ro'yxatdan o'tish sahifasi.
    URL: /accounts/register/
    """
    # Agar allaqachon login bo'lgan bo'lsa, bosh sahifaga yuborish
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Yangi foydalanuvchi yaratish
            user = form.save()

            # Profil yaratish
            Profile.objects.create(user=user)

            # Avtomatik login qilish (qayta login qilmasdan)
            login(request, user)

            messages.success(request, f'Xush kelibsiz, {user.username}! Muvaffaqiyatli ro\'yxatdan o\'tdingiz.')
            return redirect('home')
        else:
            messages.error(request, 'Xato! Iltimos, ma\'lumotlarni tekshiring.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Login sahifasi.
    URL: /accounts/login/
    """
    # Agar allaqachon login bo'lgan bo'lsa
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Foydalanuvchini tekshirish
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Xush kelibsiz, {username}!')

                # Agar /accounts/login/?next=/advanced/ bo'lsa, o'sha sahifaga yuborish
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Foydalanuvchi nomi yoki parol noto\'g\'ri!')
        else:
            messages.error(request, 'Login ma\'lumotlari noto\'g\'ri!')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Logout.
    URL: /accounts/logout/
    Faqat POST orqali (CSRF himoyasi uchun)
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Muvaffaqiyatli chiqtingiz!')
    return redirect('home')


@login_required
def profile_view(request):
    """
    Foydalanuvchi profili.
    URL: /accounts/profile/
    """
    from calculator.models import CalculationHistory

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'bio' in request.POST:
            profile.bio = request.POST['bio']
            profile.save()
            messages.success(request, 'Profil yangilandi!')
            return redirect('profile')

    total = CalculationHistory.objects.filter(user=request.user).count()
    basic_count = CalculationHistory.objects.filter(user=request.user, calculation_type='basic').count()
    advanced_count = CalculationHistory.objects.filter(user=request.user, calculation_type='advanced').count()

    return render(request, 'accounts/profile.html', {
        'total_calculations': total,
        'basic_count': basic_count,
        'advanced_count': advanced_count,
        'profile': profile,
    })


@login_required
def chat_view(request):
    """
    Suniy intellekt chat sahifasi.
    URL: /accounts/chat/
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    messages_list = ChatMessage.objects.filter(user=request.user)[:50]
    
    return render(request, 'accounts/chat.html', {
        'messages': messages_list,
        'profile': profile,
    })


@login_required
def chat_send(request):
    """
    Chat xabar yuborish API.
    URL: /accounts/chat/send/
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Faqat POST!'}, status=405)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Noto\'g\'ri JSON!'}, status=400)

    if not user_message:
        return JsonResponse({'error': 'Xabar bo\'sh!'}, status=400)

    # AI javoblarga murojaat
    response = generate_ai_response(user_message)

    # ChatMessage yaratish
    chat_msg = ChatMessage.objects.create(
        user=request.user,
        message=user_message,
        response=response
    )

    return JsonResponse({
        'message': user_message,
        'response': response,
        'time': chat_msg.created_at.strftime('%H:%M')
    })


def generate_ai_response(message):
    """Google Gemini orqali haqiqiy AI matematika javoblari (retry logic bilan)"""
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "❌ Tizimda AI ulanmagan (GEMINI_API_KEY topilmadi)."
    
    # 3 ta urinish
    for attempt in range(3):
        try:
            client = genai.Client(api_key=api_key)
            
            system_instruction = (
                "You are a highly intelligent math assistant and professor. "
                "Your task is to solve equations (e.g., 2x+5=10), higher mathematics (integrals, derivatives), "
                "algebra, and geometry examples step-by-step requested by the user. "
                "Always respond clearly, accurately, and in a friendly tone using Markdown formats. "
                "IMPORTANT: Always reply in the exact same language the user writes in. "
                "If they write in Russian, reply in Russian. If they write in English, reply in English. "
                "If they write in Uzbek, reply in Uzbek."
            )
            
            # gemini-2.0-flash stabilroq va zamonaviy
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=message,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                )
            )
            
            return response.text
            
        except Exception as e:
            error_str = str(e)
            # Agar error 503 (Unavailable) bo'lsa va urinishlar qolgan bo'lsa
            if "503" in error_str and attempt < 2:
                time.sleep(2 * (attempt + 1))  # Exponential backoff
                continue
            return f"❌ Uzr, AI tarmog'iga ulanishda xato yuz berdi (Urinish {attempt+1}/3):\n\n{error_str}"
    
    return "❌ AI bilan ulanib bo'lmadi."
