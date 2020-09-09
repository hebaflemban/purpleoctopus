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

COLOR_CHOICES =[("BL", "Black"),
                ("WH", "White"),
                ("GY", "Gray"),
                ("BR", "Browns"),
                ("GR", "Green"),
                ("BU", "Blue"),
                ("PU", "Purple"),
                ("RE", "Red"),
                ("OR", "Orange"),
                ("YE", "Yellow"),
]

class ProductForm(forms.ModelForm):
    #color = forms.MultipleChoiceField(choices = COLOR_CHOICES)

    class Meta:
        model = Product
        exclude = ['color', 'theme']
