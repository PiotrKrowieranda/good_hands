from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings


# Manager niestandardowego użytkownika
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email musi być ustawiony.")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        print("Użytkownik został utworzony")
        return user


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


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

    # Referring to settings.AUTH_USER_MODEL means using a custom user model,
    # which is defined in Django settings. In the standard Django user model, this model is typically set to auth.User.

    def __str__(self):
        return f'Donation #{self.id} - {self.quantity} bags'



