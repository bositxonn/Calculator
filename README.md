<div align="center">

<!-- LOGO / BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=MathAI%20Calculator&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=Django-powered%20smart%20calculator%20with%20Google%20Gemini%20AI&descSize=18&descAlignY=60&descColor=c9b6ff" alt="MathAI Calculator Banner"/>

<br/>

[![Stars](https://img.shields.io/github/stars/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29&logo=github)](https://github.com/bositxonn/Calculator/stargazers)
[![Forks](https://img.shields.io/github/forks/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29&logo=git)](https://github.com/bositxonn/Calculator/forks)
[![License](https://img.shields.io/github/license/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29)](LICENSE)
[![Issues](https://img.shields.io/github/issues/bositxonn/Calculator?style=for-the-badge&color=302b63&labelColor=0f0c29)](https://github.com/bositxonn/Calculator/issues)

<br/>

> **MathAI Calculator** — это веб-приложение на **Django**, объединяющее классический калькулятор,  
> высшую математику и **Google Gemini AI** в одном элегантном интерфейсе.  
> Поддерживает аутентификацию пользователей, историю вычислений и полноценный ИИ-чат.

<br/>

[✨ Функции](#-функции) · [🛠️ Технологии](#️-технологии) · [⚙️ Установка](#️-установка) · [🏗️ Архитектура](#️-архитектура) · [🗺️ Планы](#️-планы-развития)

---

</div>

<br/>

## ✨ Функции

<div align="center">

| Категория | Возможности |
|:---:|:---|
| 🔢 **Базовые вычисления** | Сложение, вычитание, умножение, деление, скобки, проценты |
| 📐 **Тригонометрия** | sin, cos, tan, arcsin, arccos, arctan + гиперболические функции |
| 📈 **Алгебра** | Степени, корни, логарифмы (log, ln, log₂) |
| ∫ **Высшая математика** | Производные, интегралы, пределы — через специальный интерфейс |
| 📜 **История** | Автоматическое сохранение всех вычислений для каждого пользователя |
| 🤖 **ИИ-чат (Gemini)** | Пошаговые объяснения, помощь с задачами, поддержка LaTeX и Markdown |
| 👤 **Профиль** | Регистрация, вход, личный профиль с биографией |
| 🔐 **JWT Auth** | Токенная аутентификация через DRF SimpleJWT |

</div>

<br/>

## 🤖 ИИ-ассистент (Google Gemini)

Встроенный чат с **Google Gemini AI** — это больше, чем просто ответы на вопросы:

- 💬 **Объясняет решения** — пошаговый разбор любой задачи
- 🧮 **Рендеринг формул** — ответы с LaTeX-формулами через MathJax
- 📝 **Markdown-поддержка** — красиво оформленные ответы с кодом и списками
- 🌐 **Многоязычность** — отвечает на языке вопроса (русский, английский, узбекский и др.)
- 💾 **История чата** — все диалоги сохраняются в БД и привязаны к аккаунту

```
Вы:   "Объясни, как взять производную от sin(x²)"
ИИ:   Используем правило цепочки: d/dx[sin(u)] = cos(u)·u',
      где u = x². Тогда u' = 2x.
      Итого: d/dx[sin(x²)] = cos(x²) · 2x
```

<br/>

## 🛠️ Технологии

<div align="center">

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django_6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![MathJax](https://img.shields.io/badge/MathJax-3.0-blue?style=for-the-badge)

</div>

| Пакет | Версия | Назначение |
|---|---|---|
| Django | 6.0.2 | Основной веб-фреймворк |
| djangorestframework | 3.16.1 | REST API |
| djangorestframework-simplejwt | 5.5.1 | JWT-аутентификация |
| google-genai | >=0.4.0 | Google Gemini AI |
| django-environ | 0.13.0 | Управление переменными окружения |
| python-dotenv | >=1.0.0 | Загрузка `.env` файла |
| Pillow | 12.1.1 | Работа с изображениями |

<br/>

## ⚙️ Установка

### Требования

- Python `>= 3.10`
- pip
- Google Gemini API ключ ([получить здесь](https://aistudio.google.com/))

### Быстрый старт

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/bositxonn/Calculator.git
cd Calculator/MathAI

# 2. Создайте и активируйте виртуальное окружение
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Настройте переменные окружения
copy .env.example .env       # Windows
# cp .env.example .env       # Linux / macOS
# Отредактируйте .env и укажите свои ключи

# 5. Примените миграции
python manage.py migrate

# 6. Создайте суперпользователя (опционально)
python manage.py createsuperuser

# 7. Запустите сервер
python manage.py runserver
```

Откройте браузер: **https://calculatorhandmade.pythonanywhere.com/**

### Переменные окружения

Создайте файл `.env` в папке `MathAI/` (на основе `.env.example`):

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Google Gemini AI
GEMINI_API_KEY=your_gemini_api_key_here

# CORS & CSRF (для продакшена)
CORS_ALLOWED_ORIGINS=http://localhost:3000
CSRF_TRUSTED_ORIGINS=https://yourdomain.com
```

<br/>

## 🏗️ Архитектура

```
📦 MathAI/                          ← Корень Django-проекта
├── 📁 calculator_project/          ← Настройки проекта
│   ├── settings.py                 # Конфигурация Django
│   ├── urls.py                     # Главный URL-роутер
│   └── wsgi.py / asgi.py
│
├── 📁 calculator/                  ← Приложение: калькулятор
│   ├── models.py                   # CalculationHistory (история вычислений)
│   ├── views.py                    # Логика вычислений
│   ├── urls.py                     # URL-маршруты
│   └── utils.py                    # Вспомогательные функции
│
├── 📁 accounts/                    ← Приложение: пользователи
│   ├── models.py                   # Profile, ChatMessage
│   ├── views.py                    # Регистрация, вход, профиль, чат
│   ├── forms.py                    # Формы регистрации и профиля
│   └── urls.py                     # URL-маршруты
│
├── 📁 templates/                   ← HTML-шаблоны
│   ├── base.html                   # Базовый шаблон
│   ├── calculator/
│   │   ├── home.html               # Главная страница калькулятора
│   │   ├── advanced.html           # Высшая математика
│   │   └── history.html            # История вычислений
│   └── accounts/
│       ├── chat.html               # ИИ-чат (Gemini)
│       └── profile.html            # Профиль пользователя
│
├── 📁 static/                      ← Статические файлы (CSS, JS)
├── 📁 config/                      ← Дополнительные конфиги
├── manage.py
├── requirements.txt
└── .env.example
```

### Модели данных

```
User (встроенный Django)
 ├── Profile (1:1)         — bio, created_at
 ├── ChatMessage (1:N)     — message, response, created_at
 └── CalculationHistory (1:N) — expression, result, calculation_type, created_at
```

<br/>

## 📖 Использование

### Базовый калькулятор

Введите выражение в поле ввода на главной странице:

```
2 + 2 * (3 - 1)    →   6
sqrt(144)           →   12
sin(pi/2)           →   1
log(100)            →   2
```

### Высшая математика

Используйте раздел **Advanced** для сложных вычислений:

```
# Производная
diff(x^3 + 2*x, x)          →   3x² + 2

# Интеграл
integrate(sin(x), x)          →   -cos(x) + C

# Предел
limit(sin(x)/x, x, 0)        →   1
```

### ИИ-чат

Зайдите в раздел **Chat** и задайте вопрос на любом языке:

```
"Помоги решить систему уравнений: x+y=5, 2x-y=1"
"What is the derivative of e^x?"
"Integralni tushuntir: ∫x²dx"
```

<br/>

## 🗺️ Планы развития

- [x] Базовые арифметические операции
- [x] Тригонометрические и логарифмические функции
- [x] История вычислений с привязкой к пользователю
- [x] ИИ-чат на базе Google Gemini
- [x] JWT-аутентификация (DRF)
- [x] Рендеринг LaTeX-формул (MathJax)
- [x] Профиль пользователя
- [ ] 📊 Построение графиков функций
- [ ] 📱 Мобильное приложение
- [ ] 🔗 Общий доступ к истории по ссылке
- [ ] 🐘 PostgreSQL в продакшене
- [ ] 🐳 Docker + docker-compose

<br/>

## 🤝 Вклад в проект

Вклад приветствуется! Вот как можно помочь:

1. 🍴 Сделайте **Fork** репозитория
2. 🌿 Создайте ветку: `git checkout -b feature/amazing-feature`
3. 💾 Зафиксируйте изменения: `git commit -m 'Add amazing feature'`
4. 📤 Отправьте ветку: `git push origin feature/amazing-feature`
5. 🔃 Откройте **Pull Request**

<br/>

## 📄 Лицензия

Распространяется под лицензией **MIT**. Подробности в файле [LICENSE](LICENSE).

<br/>

## 🙏 Благодарности

- [Google Gemini](https://deepmind.google/technologies/gemini/) — AI-движок для чата
- [Django](https://www.djangoproject.com/) — мощный Python веб-фреймворк
- [DRF SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/) — JWT-аутентификация
- [MathJax](https://www.mathjax.org/) — рендеринг математических формул

<br/>

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=100&section=footer" alt="footer"/>

**Сделано с ❤️ и ∞ математики**

⭐ Если проект понравился — не забудьте поставить звезду!

</div>
