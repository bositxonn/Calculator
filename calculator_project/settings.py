# calculator_project/settings.py
# Bu Django loyihasining asosiy sozlamalari fayli

from pathlib import Path

# Loyiha papkasining asosiy yo'li
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ MUHIM: Production'da bu kalitni o'zgartiring va .env faylga ko'chiring!
SECRET_KEY = 'django-insecure-calculator-loyiha-2024-bu-kalitni-ozgartiring'

# Ishlab chiqishda True, production'da False bo'lishi SHART
DEBUG = True

# Production'da bu yerga o'zingizning domeningizni yozing
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Qo'shilgan ilovalar (apps)
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin panel
    'django.contrib.auth',         # Login/logout tizimi
    'django.contrib.contenttypes', # Content types
    'django.contrib.sessions',     # Session boshqaruvi
    'django.contrib.messages',     # Flash messages
    'django.contrib.staticfiles',  # Static fayllar (CSS, JS)
    'calculator',                  # Bizning kalkulyator ilovasi
    'accounts',                    # Bizning auth ilovasi
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',        # CSRF xujumlaridan himoya
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'calculator_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates papkasi
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calculator_project.wsgi.application'

# Ma'lumotlar bazasi - SQLite (oddiy, o'rnatish shart emas)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Bu fayl avtomatik yaratiladi
    }
}

# Parol tekshirish qoidalari
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'uz'       # O'zbek tili
TIME_ZONE = 'Asia/Tashkent'  # Toshkent vaqti
USE_I18N = True
USE_TZ = True

# Static fayllar (CSS, JS) joylashuvi
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media fayllar (rasmlar)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/logout yo'nalishlari
LOGIN_URL = '/accounts/login/'           # Login bo'lmasa shu sahifaga yuboradi
LOGIN_REDIRECT_URL = '/'                 # Login bo'lgandan keyin bosh sahifaga
LOGOUT_REDIRECT_URL = '/'               # Logout bo'lgandan keyin bosh sahifaga
