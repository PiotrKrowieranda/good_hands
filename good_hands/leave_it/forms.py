# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password1', 'password2')
#
# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')
#
# class CustomPasswordChangeForm(PasswordChangeForm):
#     class Meta:
#         model = CustomUser

class UserRegistrationForm(forms.Form):
    """
    Formularz rejestracji użytkownika.
    """

    login = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_login(self):
        login = self.cleaned_data.get('login')

        if User.objects.filter(username=login).exists():
            raise ValidationError("Login jest już zajęty.")
        if not login:
            raise forms.ValidationError("To pole jest wymagane.")

        return login

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise ValidationError("Hasła nie są identyczne.")
        if not password and password_confirm:
            raise forms.ValidationError("To pole jest wymagane.")
