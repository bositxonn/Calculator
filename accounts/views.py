# accounts/views.py
# Login, logout, register sahifalari - 3-kishi (Dilshod) yozadi

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        if 'image' in request.FILES:
            # Eski rasmni o'chirish (default emas)
            if profile.image and profile.image.name != 'default.png':
                try:
                    profile.image.delete()
                except:
                    pass
            profile.image = request.FILES['image']
        if 'bio' in request.POST:
            profile.bio = request.POST['bio']
        profile.save()
        messages.success(request, 'Profil yangilandi!')
        return redirect('profile')
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
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
        except:
            return JsonResponse({'error': 'Noto\'g\'ri JSON!'}, status=400)

        if not user_message:
            return JsonResponse({'error': 'Xabar bo\'sh!'}, status=400)

        # AI javob (sodda simulyatsiya - real AI ulash uchun API kalit kerak)
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

    return JsonResponse({'error': 'Faqat POST!'}, status=405)


from django.http import JsonResponse
import re
import math
import random

def generate_ai_response(message):
    """Kengaytirilgan AI - algebra, geometriya, oliy matematika"""
    msg = message.lower().strip()
    
    # === GEOMETRIYA ===
    # To'g'ri burchakli uchburchak gipotenuzasi
    katet = re.findall(r'(\d+)', msg)
    if 'gipotenuza' in msg and len(katet) >= 2:
        a, b = int(katet[0]), int(katet[1])
        g = math.sqrt(a**2 + b**2)
        return f"📐 To'g'ri burchakli uchburchak gipotenuzasi:\n\na = {a}, b = {b}\nc = √({a}² + {b}²) = √({a**2} + {b**2}) = √{a**2+b**2} ≈ {round(g, 2)}"
    
    # Aylana uzunligi
    if 'aylan' in msg and 'uzunlik' in msg:
        radius = re.search(r'r\s*=\s*(\d+)', msg)
        if not radius:
            radius = re.search(r'(\d+)\s*sm', msg)
        if radius:
            r = int(radius.group(1))
            l = 2 * math.pi * r
            return f"📐 Aylana uzunligi:\nL = 2πr = 2 × {math.pi:.4f} × {r} ≈ {round(l, 2)}"
    
    # Doira yuzasi
    if 'doira' in msg and ('yuza' in msg or 'maydon' in msg):
        radius = re.search(r'r\s*=\s*(\d+)', msg)
        if not radius:
            radius = re.search(r'(\d+)\s*sm', msg)
        if radius:
            r = int(radius.group(1))
            s = math.pi * r**2
            return f"📐 Doira yuzasi:\nS = πr² = {math.pi:.4f} × {r}² = {math.pi:.4f} × {r**2} ≈ {round(s, 2)}"
    
    # Parallelogram yuzasi
    if 'parallelogramm' in msg and 'yuza' in msg:
        if len(katet) >= 2:
            a, b = int(katet[0]), int(katet[1])
            s = a * b
            return f"📐 Parallelogram yuzasi:\nS = a × h = {a} × {b} = {s}"
    
    # Trapetsiya yuzasi
    if 'trapetsiya' in msg and 'yuza' in msg:
        if len(katet) >= 2:
            a, b = int(katet[0]), int(katet[1])
            h = katet[2] if len(katet) > 2 else 1
            s = (a + b) / 2 * h
            return f"📐 Trapetsiya yuzasi:\nS = (a + b)/2 × h = ({a} + {b})/2 × {h} = {round(s, 2)}"
    
    # Piramida hajmi
    if 'piramida' in msg and ('hajm' in msg or 'volume' in msg):
        if len(katet) >= 2:
            s = int(katet[0])
            h = int(katet[1])
            v = (s * h) / 3
            return f"📐 Piramida hajmi:\nV = (S_asos × h) / 3 = ({s} × {h}) / 3 = {round(v, 2)}"
    
    # Shar hajmi
    if 'shar' in msg and ('hajm' in msg or 'volume' in msg):
        radius = re.search(r'r\s*=\s*(\d+)', msg)
        if radius:
            r = int(radius.group(1))
            v = (4/3) * math.pi * r**3
            return f"📐 Shar hajmi:\nV = (4/3)πr³ = (4/3) × {math.pi:.4f} × {r}³ ≈ {round(v, 2)}"
    
    # Kub hajmi
    if 'kub' in msg and ('hajm' in msg or 'volume' in msg):
        if katet:
            a = int(katet[0])
            return f"📐 Kub hajmi:\nV = a³ = {a}³ = {a**3}"
    
    # To'g'ri burchakli parallelepiped hajmi
    if 'parallelepiped' in msg and 'hajm' in msg:
        if len(katet) >= 3:
            a, b, h = int(katet[0]), int(katet[1]), int(katet[2])
            v = a * b * h
            return f"📐 To'g'ri burchakli parallelepiped hajmi:\nV = a × b × h = {a} × {b} × {h} = {v}"
    
    # === ALGEBRA ===
    # Kvadrat tenglama
    kvad = re.search(r'x²\s*([+-])\s*(\d+)\s*([+-])\s*(\d+)\s*=\s*0', msg)
    if not kvad:
        kvad = re.search(r'(\d+)x²\s*([+-])\s*(\d+)x\s*([+-])\s*(\d+)\s*=\s*0', msg)
    if kvad:
        return "📊 Kvadrat tenglama yechimi:\n\nTenglamani diskriminant orqali yechaman:\nD = b² - 4ac\n\nIltimos, tenglamani aniqroq yozing (masalan: x² + 5x + 6 = 0)"
    
    # Foiz hisoblash
    foiz = re.search(r'(\d+)\s*%.*?(\d+)', msg)
    if 'foiz' in msg or '%' in msg:
        if foiz:
            p = int(foiz.group(1))
            s = int(foiz.group(2))
            result = p * s / 100
            return f"📊 Foiz hisoblash:\n{p}% × {s} = ({p} × {s}) / 100 = {result}"
    
    # === OLIY MATEMATIKA ===
    # Trigonometriya hisoblash
    tr = re.search(r'sin\s*(\d+)', msg)
    if tr:
        d = int(tr.group(1))
        r = math.sin(math.radians(d))
        return f"📐 Trigonometriya:\nsin({d}°) = sin({d} × π/180) = {round(r, 6)}"
    
    tr = re.search(r'cos\s*(\d+)', msg)
    if tr:
        d = int(tr.group(1))
        r = math.cos(math.radians(d))
        return f"📐 Trigonometriya:\ncos({d}°) = cos({d} × π/180) = {round(r, 6)}"
    
    tr = re.search(r'tan\s*(\d+)', msg)
    if tr:
        d = int(tr.group(1))
        if d == 90:
            return "❌ tan(90°) aniqlanmagan (cheksiz)"
        r = math.tan(math.radians(d))
        return f"📐 Trigonometriya:\ntan({d}°) = tan({d} × π/180) = {round(r, 6)}"
    
    # Logarifm
    if 'ln' in msg:
        lg = re.search(r'ln\s*(\d+\.?\d*)', msg)
        if lg:
            x = float(lg.group(1))
            if x <= 0:
                return "❌ Logarifm faqat musbat sonlar uchun!"
            return f"📐 Natural logarifm:\nln({x}) = {round(math.log(x), 6)}"
    
    if 'log' in msg and 'ln' not in msg:
        lg = re.search(r'log\s*(\d+)', msg)
        if lg:
            x = int(lg.group(1))
            if x <= 0:
                return "❌ Logarifm faqat musbat sonlar uchun!"
            return f"📐 O'nlik logarifm:\nlog₁₀({x}) = {round(math.log10(x), 6)}"
    
    # Ildiz
    ildiz = re.search(r'√(\d+)', msg.replace('sqrt ', ''))
    if not ildiz:
        ildiz = re.search(r'ildiz.*?(\d+)', msg)
    if ildiz:
        n = int(ildiz.group(1))
        return f"📐 Ildiz:\n√{n} = {round(math.sqrt(n), 6)}"
    
    # Daraja
    daraja = re.search(r'(\d+)\s*\^\s*(\d+)', msg.replace('^', ' ^ '))
    if not daraja:
        daraja = re.search(r'(\d+)\s*daraja\s*(\d+)', msg)
    if daraja:
        n = int(daraja.group(1))
        p = int(daraja.group(2))
        return f"📐 Daraja:\n{n}^{p} = {n**p}"
    
    # === SODDA ARIFMETIKA ===
    patterns = [
        (r'(\d+)\s*\+\s*(\d+)', lambda m: int(m.group(1)) + int(m.group(2)), "yig'indi"),
        (r'(\d+)\s*minus\s*(\d+)', lambda m: int(m.group(1)) - int(m.group(2)), "ayirma"),
        (r'(\d+)\s*\*\s*(\d+)', lambda m: int(m.group(1)) * int(m.group(2)), "ko'paytma"),
        (r'(\d+)\s*/\s*(\d+)', lambda m: round(int(m.group(1)) / int(m.group(2)), 4) if int(m.group(2)) != 0 else "Xato", "bo'linma"),
    ]
    
    for pattern, calc, info in patterns:
        match = re.search(pattern, msg)
        if match:
            try:
                result = calc(match)
                if result != "Xato":
                    return f"✅ Hisoblash natijasi:\n\n{match.group(0)} = {result} ({info})"
                else:
                    return "❌ Nolga bo'lish mumkin emas!"
            except:
                pass
    
    # Kvadrat
    kvadrat = re.search(r'(\d+)\s*(ni|ning)\s*kvadrati?', msg)
    if kvadrat:
        n = int(kvadrat.group(1))
        return f"✅ Hisoblash natijasi:\n\n{n}² = {n*n} ({n} × {n})"
    
    # Kub
    kub = re.search(r'(\d+)\s*(ni|ning)\s*kub', msg)
    if kub:
        n = int(kub.group(1))
        return f"✅ Hisoblash natijasi:\n\n{n}³ = {n*n*n} ({n} × {n} × {n})"
    
    # Faktorial
    fact = re.search(r'(\d+)!', msg)
    if fact:
        n = int(fact.group(1))
        if n > 20:
            return "❌ Faktorial 20 dan katta bo'lishi mumkin emas!"
        return f"✅ Hisoblash natijasi:\n\n{n}! = {math.factorial(n)}"
    
    # === ODDIY JAVOBLAR ===
    responses = {
        'salom': ['Salom! 👋 Matematika yoki geometriya bo\'yicha savolingiz bormi?', 'Salom! Qanday yordam berishim mumkin?'],
        'qanday': ['Yaxshi, rahmat! 😊 Sizga qanday yordam kerak?', 'Zo\'r! Matematik savollar berishingiz mumkin.'],
        'rahmat': ['Marhamat! 😊', 'Xizmat uchun!', 'Arzigul!'],
        'kim': ['Men suniy intellektman - matematika, geometriya va oliy matematika bo\'yicha yordam beraman!'],
        'yordam': ['Albatta! Hisoblash, geometriya yoki algebra bo\'yicha savol berishingiz mumkin.'],
    }
    
    for key, resp_list in responses.items():
        if key in msg:
            return random.choice(resp_list)
    
    # Yordam berish
    return """📚 Men quyidagi sohalarda yordam berishim mumkin:

🧮 Oddiy arifmetika: 5 + 3, 10 * 2, 8 - 4
📐 Kvadrat va kub: 5 ni kvadrati, 3 ni kubi
🌿 Ildiz: √16, ildiz 25
❗ Daraja: 2^10, 3^8
❗ Faktorial: 5!
📊 Foiz: 20% ni 50 dan
🔺 Geometriya:
   - Uchburchak perimetri
   - Aylana uzunligi (r=5)
   - Doira yuzasi (r=3)
   - Kub hajmi (a=4)
   - Shar hajmi (r=2)
📈 Oliy matematika:
   - sin(30°), cos(45°), tan(60°)
   - ln(2), log(100)
   - Ildiz va darajalar

Misol yozing! 😊"""
