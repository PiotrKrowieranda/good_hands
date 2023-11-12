from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings

# Manager niestandardowego użytkownika
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        # Sprawdź, czy podano adres e-mail
        if not email:
            raise ValueError("Pole Email musi być wypełnione")

        # Znormalizuj adres e-mail
        email = self.normalize_email(email)

        # Stwórz nowego użytkownika
        user = self.model(email=email, username=email, **extra_fields)

        # Sprawdź, czy podano hasło
        if not password:
            raise ValueError("Pole hasło musi być wypełnione")

        user.set_password(password)  # Ustawienie hasła użytkownika
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Tworzenie superużytkownika
        """Metoda setdefault to metoda słownika . Służy do pobierania wartości danego klucza z słownika.
         Jeśli klucz nie istnieje, setdefault dodaje klucz do słownika z podaną wartością domyślną."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        #Jeśli w słowniku extra_fields nie istnieje klucz 'is_staff' lub 'is_superuser', to metoda setdefault doda te klucze do słownika
        # i ustawi ich wartość na True. Jeśli klucze te już istnieją,
        # to metoda nie wprowadzi żadnych zmian. W ten sposób zapewniamy, że atrybuty 'is_staff' i 'is_superuser'
        # są dostępne w słowniku extra_fields i mają domyślne wartości True, jeśli nie są już ustawione.

# Niestandardowy model użytkownika
class CustomUser(AbstractUser):
    # Dodanie pola e-mail jako unikalnego
    email = models.EmailField(unique=True)

    # Ustawienie managera
    objects = CustomUserManager()

    # Ustawienie pola e-mail jako nazwy użytkownika (logowanie)
    USERNAME_FIELD = 'email'

    # Lista pól wymaganych podczas tworzenia użytkownika moża dodać np telefon ale teraz jest puste - żadne dodatkowe pola nie są wymagane podczas tworzenia użytkownika.
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email  # Reprezentacja obiektu jako ciąg znaków


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Institution(models.Model):
    TYPE_CHOICES = [
        ('fundacja', 'Fundacja'),
        ('organizacja', 'Organizacja Pozarządowa'),
        ('zbiórka', 'Zbiórka Lokalna'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='fundacja')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    #Odniesienie do settings.AUTH_USER_MODEL oznacza używanie niestandardowego modelu użytkownika,
    #który jest zdefiniowany w ustawieniach Django. W standardowym modelu użytkownika Django, model ten jest zazwyczaj ustawiany na auth.User.

    def __str__(self):
        return f'Donation #{self.id} - {self.quantity} bags'  # Reprezentacja obiektu jako ciąg znaków
