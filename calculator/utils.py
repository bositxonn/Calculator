# calculator/utils.py
# Barcha matematik hisoblashlar shu yerda - 2-kishi (Jasur) yozadi

import math


def calculate_basic(expression):
    """
    Oddiy amallar: +, -, *, /, %
    Hamma foydalanuvchi ishlatishi mumkin.

    expression: "2 + 3" yoki "10 / 2"
    Qaytaradi: (natija, xato_xabari)
    """
    try:
        # Faqat ruxsat etilgan belgilar
        allowed = set('0123456789+-*/.% ()')
        if not all(c in allowed for c in expression):
            return None, "Noto'g'ri belgi ishlatildi!"

        # eval() xavfsiz ishlatish uchun tekshirish
        if '__' in expression or 'import' in expression:
            return None, "Bu ifoda ruxsat etilmagan!"

        result = eval(expression)  # noqa

        # Natija cheksizmi?
        if math.isinf(result):
            return None, "Nolga bo'lish mumkin emas!"

        # Butun son bo'lsa, kasr qismini ko'rsatma
        if isinstance(result, float) and result.is_integer():
            return str(int(result)), None

        return str(round(result, 10)), None

    except ZeroDivisionError:
        return None, "Nolga bo'lish mumkin emas!"
    except Exception:
        return None, "Noto'g'ri ifoda!"


def calculate_advanced(func_name, value, base=None):
    """
    Oliy matematika funksiyalari.
    FAQAT login bo'lgan foydalanuvchilar uchun!

    func_name: 'log', 'log2', 'log10', 'sin', 'cos', 'tan', 'sqrt', 'pow', 'factorial'
    value: asosiy son
    base: log uchun asos (ixtiyoriy)
    Qaytaradi: (natija, xato_xabari)
    """
    try:
        value = float(value)

        if func_name == 'log':
            # log(x) = natural logarifm
            if value <= 0:
                return None, "Logarifm faqat musbat sonlar uchun!"
            if base:
                result = math.log(value, float(base))
                expr = f"log_{base}({value})"
            else:
                result = math.log(value)
                expr = f"ln({value})"

        elif func_name == 'log10':
            # log10(x) = o'nlik logarifm
            if value <= 0:
                return None, "Logarifm faqat musbat sonlar uchun!"
            result = math.log10(value)
            expr = f"log₁₀({value})"

        elif func_name == 'log2':
            # log2(x) = ikkilik logarifm
            if value <= 0:
                return None, "Logarifm faqat musbat sonlar uchun!"
            result = math.log2(value)
            expr = f"log₂({value})"

        elif func_name == 'sin':
            # sin(x) - x daraja (degree) da
            result = math.sin(math.radians(value))
            expr = f"sin({value}°)"

        elif func_name == 'cos':
            # cos(x) - x daraja (degree) da
            result = math.cos(math.radians(value))
            expr = f"cos({value}°)"

        elif func_name == 'tan':
            # tan(x) - x daraja (degree) da
            if value % 180 == 90:
                return None, "tan(90°) mavjud emas!"
            result = math.tan(math.radians(value))
            expr = f"tan({value}°)"

        elif func_name == 'sqrt':
            # sqrt(x) = kvadrat ildiz
            if value < 0:
                return None, "Manfiy sonning ildizi mavjud emas!"
            result = math.sqrt(value)
            expr = f"√({value})"

        elif func_name == 'pow':
            # pow(x, n) = x ning n darajasi
            if base is None:
                return None, "Daraja ko'rsatilmadi!"
            result = math.pow(value, float(base))
            expr = f"{value}^{base}"

        elif func_name == 'factorial':
            # n! = faktorial
            n = int(value)
            if n < 0:
                return None, "Manfiy sonning faktorialini hisoblash mumkin emas!"
            if n > 20:
                return None, "Juda katta son! (max: 20)"
            result = math.factorial(n)
            expr = f"{n}!"

        elif func_name == 'pi':
            # Pi soni
            result = math.pi
            expr = "π"

        elif func_name == 'e':
            # Eyler soni
            result = math.e
            expr = "e"

        elif func_name == 'exp':
            # exp(x) = e^x
            result = math.exp(value)
            expr = f"e^{value}"

        elif func_name == 'cbrt':
            # Kubik ildiz
            result = math.copysign(abs(value) ** (1/3), value)
            expr = f"∛({value})"

        elif func_name == 'abs':
            # Absolut qiymat
            result = abs(value)
            expr = f"|{value}|"

        elif func_name == 'floor':
            # Eng katta butun son
            result = math.floor(value)
            expr = f"⌊{value}⌋"

        elif func_name == 'ceil':
            # Eng kichik butun son
            result = math.ceil(value)
            expr = f"⌈{value}⌉"

        elif func_name == 'round':
            # Yaqinlashgan butun son
            result = round(value)
            expr = f"round({value})"

        elif func_name == 'deg':
            # Radian -> Daraja
            result = math.degrees(value)
            expr = f"{value} rad → °"

        elif func_name == 'rad':
            # Daraja -> Radian
            result = math.radians(value)
            expr = f"{value}° → rad"

        elif func_name == 'sinh':
            # Giperbolik sinus
            result = math.sinh(value)
            expr = f"sinh({value})"

        elif func_name == 'cosh':
            # Giperbolik kosinus
            result = math.cosh(value)
            expr = f"cosh({value})"

        elif func_name == 'tanh':
            # Giperbolik tangens
            result = math.tanh(value)
            expr = f"tanh({value})"

        elif func_name == 'asin':
            # Arcsin (darajada)
            if value < -1 or value > 1:
                return None, "Asin faqat -1 dan 1 gacha qiymatlar uchun!"
            result = math.degrees(math.asin(value))
            expr = f"arcsin({value})"

        elif func_name == 'acos':
            # Arccos (darajada)
            if value < -1 or value > 1:
                return None, "Acos faqat -1 dan 1 gacha qiymatlar uchun!"
            result = math.degrees(math.acos(value))
            expr = f"arccos({value})"

        elif func_name == 'atan':
            # Arctan (darajada)
            result = math.degrees(math.atan(value))
            expr = f"arctan({value})"

        else:
            return None, "Noma'lum funksiya!"

        # Natijani formatlash
        if isinstance(result, float):
            if result.is_integer():
                formatted = str(int(result))
            else:
                formatted = str(round(result, 8))
        else:
            formatted = str(result)

        return formatted, expr  # (natija, ifoda) qaytaramiz

    except ValueError as e:
        return None, f"Xato qiymat: {str(e)}"
    except Exception as e:
        return None, f"Hisoblash xatosi: {str(e)}"
