# accounts/forms.py
# Ro'yxatdan o'tish va login formalari - 3-kishi (Dilshod) yozadi

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    """
    Ro'yxatdan o'tish formasi.
    Django'ning UserCreationForm'ini kengaytirdik.
    """

    # Email majburiy qilamiz
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'email@example.com'
        }),
        label='Email'
    )

    # Username uchun maxsus stil
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'foydalanuvchi_nomi'
        }),
        label='Foydalanuvchi nomi'
    )

    # Parol
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••'
        }),
        label='Parol'
    )

    # Parolni tasdiqlash
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••'
        }),
        label='Parolni tasdiqlang'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Email allaqachon mavjudmi tekshirish"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email allaqachon ro\'yxatdan o\'tgan!')
        return email

    def clean_username(self):
        """Username allaqachon mavjudmi tekshirish"""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu foydalanuvchi nomi band!')
        return username


class LoginForm(AuthenticationForm):
    """
    Login formasi.
    Django'ning AuthenticationForm'ini kengaytirdik.
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Foydalanuvchi nomi'
        }),
        label='Foydalanuvchi nomi'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••'
        }),
        label='Parol'
    )
