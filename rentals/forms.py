from django import forms
from django.contrib.auth.models import User
from .models import Product, Theme, Color

class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(required = True, widget = forms.PasswordInput())


class MembershipForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widget = {
            'password' : forms.PasswordInput(),
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'


class ProductForm(forms.ModelForm):
    #color = forms.MultipleChoiceField(choices = COLOR_CHOICES)

    class Meta:
        model = Product
        fields = '__all__'
