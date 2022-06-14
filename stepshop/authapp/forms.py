from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ShopUserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин...',
                'id': 'login',
            }
        )
    )
    first_name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя...',
                'id': 'name',
            }
        )
    )

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password1',
            }
        )
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password2',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Введите email...',
                'id': 'email',
            }
        )
    )

    age = forms.IntegerField(
        validators=[MaxValueValidator(100),
                    MinValueValidator(0)],
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Возраст...',
                'id': 'age',
                'min': 0,
                'max': 100,
            }
        )
    )

    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Вы слишком молоды...')

        return data


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'email', 'age', 'avatar', 'password'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Вы слишком молоды...')

        return data
