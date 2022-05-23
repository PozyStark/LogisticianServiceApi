from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.forms import TextInput
import numbers

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

    phone_number = forms.CharField(label='Введите номер телефона',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Введите номер телефона'
                                   }))

    class Meta:
        model = Order
        fields = ['address', 'mass', 'phone_number', 'orderer', 'state']
        widgets = {
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            # 'phone_number': CharField(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введите номер телефона'
            # }),
            'mass': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите массу заказа'
            })
        }

    def clean(self):
        cd = super().clean()
        print(cd.get('phone_number'))
        if cd.get('phone_number') is None or type(cd.get('phone_number')) != int:
            self.add_error('phone_number', 'Введите номер телефона')

