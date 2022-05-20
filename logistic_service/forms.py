from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.forms import TextInput

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean(self):
        cd = super().clean()

        if cd.get('password') != cd.get('password2'):
            self.add_error('password', 'Пароли не совпадают')

class OrdrsForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['address', 'mass', 'phone_number', 'orderer', 'state']
        widgets = {
            'address': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите адрес'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            'mass': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите массу заказа'
            })
        }
