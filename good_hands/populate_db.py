# Importuj modele
from leave_it.models import Category, Institution




# Pobierz lub utwórz kategorie
fundacja_category, _ = Category.objects.get_or_create(name="Fundacja")
organizacja_category, _ = Category.objects.get_or_create(name="Organizacja pozarządowa")
zbiorka_category, _ = Category.objects.get_or_create(name="Zbiórka lokalna")

inst1 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 1'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="jedzenie, ubrania"
)
inst1.categories.add(fundacja_category)

inst2 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 2'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="jedzenie, ubrania",
)
inst2.categories.add(organizacja_category)

inst3 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 3'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="jedzenie, ubrania"
)
inst3.categories.set([zbiorka_category])

inst4 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 4'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst4.categories.set([fundacja_category])

inst5 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 5'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst5.categories.set([organizacja_category])

inst6 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 6'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst6.categories.set([zbiorka_category])

inst7 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 7'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst7.categories.set([zbiorka_category])

inst8 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 8'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst8.categories.set([fundacja_category])

inst9 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 9'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst9.categories.set([organizacja_category])

inst10 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 10'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst10.categories.set([zbiorka_category])

inst11 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 11'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst11.categories.set([fundacja_category])

inst12 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 12'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst12.categories.set([organizacja_category])

inst13 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 13'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst13.categories.set([zbiorka_category])





inst111 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 111'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst111.categories.set([fundacja_category])

inst222 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 222'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst222.categories.set([organizacja_category])

inst333 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 333'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst333.categories.set([zbiorka_category])

inst444 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 444'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst444.categories.set([fundacja_category])

inst555 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 555'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst555.categories.set([organizacja_category])

inst666 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 666'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst666.categories.set([zbiorka_category])

inst777 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 777'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst777.categories.set([zbiorka_category])

inst888 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 888'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst888.categories.set([fundacja_category])

inst999 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 999'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst999.categories.set([organizacja_category])

inst1000 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 1000'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst1000.categories.set([zbiorka_category])

inst1133 = Institution.objects.create(
    name="Fundacja 'Lorem Ipsum 1133'",
    description="Cel i misja: Pomoc dla potrzebujących.",
    type="fundacja",
)
inst1133.categories.set([fundacja_category])

inst1552 = Institution.objects.create(
    name="Organizacja 'Lorem Ipsum 1552'",
    description="Cel i misja: Pomoc dla osób chorych.",
    type="organizacja",
)
inst1552.categories.set([organizacja_category])

inst1377 = Institution.objects.create(
    name="Zbiórka 'Lorem Ipsum 1377'",
    description="Cel i misja: Pomoc dla zwierząt.",
    type="zbiórka",
)
inst1377.categories.set([zbiorka_category])





# Wyświetl wszystkie instytucje
Institution.objects.all()

# instytucje z kategoriami


categories = Category.objects.all()
for category in categories:
    print(f"Kategoria: {category.name}, ID: {category.id}")
    # Pobieramy instytucje przypisane do tej kategorii
    institutions = category.institution_set.all()
    for institution in institutions:
        print(f"    Instytucja: {institution.name} ")


#stworzenie donacji o ilości 5 i przypisznie do każdej instytucji

from leave_it.models import Institution, Donation
from django.utils import timezone

# Pobieramy instytucje
institutions = Institution.objects.all()

# Tworzymy donacje i przypisujemy im datę i czas
for institution in institutions:
    Donation.objects.create(
        quantity=5,
        institution=institution,
        pick_up_date=timezone.now().date(),  # Ustawiamy datę bieżącą
        pick_up_time=timezone.now().time()   # Ustawiamy czas bieżący
    )


# sprawdzenie datków

from leave_it.models import Donation

# Pobieramy wszystkie donacje wraz z informacją o instytucjach
donations = Donation.objects.all()

# Iterujemy przez donacje
for donation in donations:
    print(f"Donacja ID: {donation.id}")
    print(f"Ilość: {donation.quantity}")
    print(f"Instytucja: {donation.institution.name}")  # Zakładając, że nazwa instytucji jest przechowywana w polu 'name'
    print(f"Adres: {donation.address}")
    print(f"Numer telefonu: {donation.phone_number}")
    print(f"Miasto: {donation.city}")
    print(f"Kod pocztowy: {donation.zip_code}")
    print(f"Data odbioru: {donation.pick_up_date}")
    print(f"Czas odbioru: {donation.pick_up_time}")
    print(f"Komentarz: {donation.pick_up_comment}")
    print("----------------------------------------")
