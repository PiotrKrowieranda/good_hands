
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.core.exceptions import ValidationError

# from .forms import CustomUserCreationForm

# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Użytkownik został pomyślnie zalogowany')
            return redirect('index')
        else:
            messages.error(request, 'Nieprawidłowe dane logowania.')
            return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # Pobierz dane z formularza
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Sprawdź, czy hasła są takie same
        if password != password2:
            messages.error(request, 'Hasła nie są identyczne')
            return render(request, 'register.html')

        # Stwórz użytkownika
        user = CustomUser.objects.create_user(email=email, password=password)
        user.name = name
        user.surname = surname
        user.save()

        messages.success(request, 'Użytkownik został pomyślnie zarejestrowany')
        return redirect('login')

class ResetPasswordView(View):
    def get(self, request):
        return render(request, "reset_password.html")

    def post(self, request):
        # Pobierz dane z żądania
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Sprawdź, czy hasła są identyczne
        if password != password_confirm:
            messages.error(request, 'Hasła nie są identyczne.')
            return render(request, "reset_password.html")

        # Tutaj dodaj logikę resetowania hasła, np. wysłanie e-maila z linkiem resetującym
        # ...

        # Po zresetowaniu hasła dodaj komunikat sukcesu
        messages.success(request, 'Hasło zostało zresetowane. Zaloguj się nowym hasłem.')

        # Przekieruj na stronę indeksu lub inną
        return redirect('login')
# z FORMULARZA
# class RegistrationView(View):
#
#     def get(self, request):
#         form = CustomUserCreationForm()
#         return render(request, 'register.html', {'form': form})
#
#     def post(self, request):
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Użytkownik został pomyślnie zarejestrowany.")
#             # Przekierowanie na stronę logowania z komunikatem success
#             return redirect('login')
#         else:
#             return render(request, 'register.html', {'form': form})
