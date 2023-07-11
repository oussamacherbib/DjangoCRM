from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email-address'}),
                             required=True)
    first_name = forms.CharField(max_length=30, label="",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First-name'}),
                                 required=True)
    last_name = forms.CharField(max_length=30, label="",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last-name'}),
                                required=True)

    class Meta:
        model = UserCreationForm
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), }
        labels = {'username': '', 'password1': '', 'password2': '', }
