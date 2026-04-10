# accounts/views.py
# Login, logout, register sahifalari - 3-kishi (Dilshod) yozadi

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm


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

    # Statistika hisoblash
    total = CalculationHistory.objects.filter(user=request.user).count()
    basic_count = CalculationHistory.objects.filter(user=request.user, calculation_type='basic').count()
    advanced_count = CalculationHistory.objects.filter(user=request.user, calculation_type='advanced').count()

    return render(request, 'accounts/profile.html', {
        'total_calculations': total,
        'basic_count': basic_count,
        'advanced_count': advanced_count,
    })
