
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


from django.http import JsonResponse
from .models import Institution, Category

class GetInstitutionsView(View):
    def get(self, request):
        category_id = request.GET.get('category', None)
        if category_id:
            institutions = Institution.objects.filter(categories__id=category_id)
        else:
            institutions = Institution.objects.all()

        data = []

        for institution in institutions:
            data.append({
                'name': institution.name,
                'description': institution.description,
                'details': institution.type,
            })

        return JsonResponse(data, safe=False)


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')

class AddDonationView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'leave_it.add_donation'
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

        if not email:
            messages.error(request, 'Pole jest wymagane')
            return render(request, 'register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "email jest już zajęty.")
            return render(request, 'register.html')

        # Sprawdź, czy hasła są takie same
        if password != password2:
            messages.error(request, 'Hasła nie są identyczne')
            return render(request, 'register.html')

        if not password and password2:
            messages.error(request, 'Pole jest wymagane')
            return render(request, 'register.html')

        # Stwórz użytkownika
        try:
            user = CustomUser.objects.create_user(email=email, password=password)
            user.name = name
            user.surname = surname
            user.save()

            messages.success(request, 'Użytkownik został pomyślnie zarejestrowany')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Wystąpił błąd podczas rejestracji: {e}')
            return render(request, 'register.html')

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

