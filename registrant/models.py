from django.db import models


class Registrant(models.Model):

    DOCTOR = 'Dr.'
    MISS = 'Ms.'
    MISTER = 'Mr.'
    TITLE_CHOICES = (
        (DOCTOR, 'Dr.'),
        (MISS, 'Ms.'),
        (MISTER, 'Mr.')
    )

    MEALPACK = 'mealpack'
    DINNER_DAY_2 = 'dinnerday2'
    MEAL_CHOICES = (
        (MEALPACK, 'mealpack'),
        (DINNER_DAY_2, 'dinnerday2')
    )

    WORKSHOP_A = 'Workshop A'
    WORKSHOP_B = 'Workshop B'
    WORKSHOP_C = 'Workshop C'
    SESSION_1_CHOICES = (
        (WORKSHOP_A, 'Workshop A'),
        (WORKSHOP_B, 'Workshop B'),
        (WORKSHOP_C, 'Workshop C')
    )

    WORKSHOP_D = 'Workshop D'
    WORKSHOP_E = 'Workshop E'
    WORKSHOP_F = 'Workshop F'
    SESSION_2_CHOICES = (
        (WORKSHOP_D, 'Workshop D'),
        (WORKSHOP_E, 'Workshop E'),
        (WORKSHOP_F, 'Workshop F')
    )

    WORKSHOP_G = 'Workshop G'
    WORKSHOP_H = 'Workshop H'
    WORKSHOP_I = 'Workshop I'
    SESSION_3_CHOICES = (
        (WORKSHOP_G, 'Workshop G'),
        (WORKSHOP_H, 'Workshop H'),
        (WORKSHOP_I, 'Workshop I')
    )

    AMERICAN_EXPRESS = 'AE'
    MASTER_CARD = 'MC'
    VISA = 'V'
    CREDIT_CARD_CHOICES = (
        (AMERICAN_EXPRESS, 'AE'),
        (MASTER_CARD, 'MC'),
        (VISA, 'V')
    )

    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)
    website = models.URLField(max_length=50)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    meals = models.CharField(max_length=30, choices=MEAL_CHOICES)
    billing_firstname = models.CharField(max_length=30)
    billing_lastname = models.CharField(max_length=30)
    card_type = models.CharField(max_length=15, choices=CREDIT_CARD_CHOICES)
    card_number = models.CharField(max_length=30)
    card_csv = models.CharField(max_length=4)
    exp_year = models.CharField(max_length=4)
    exp_month = models.CharField(max_length=2)
    session1 = models.CharField(max_length=30, choices=SESSION_1_CHOICES)
    session2 = models.CharField(max_length=30, choices=SESSION_2_CHOICES)
    session3 = models.CharField(max_length=30, choices=SESSION_3_CHOICES)
    date_of_registration = models.DateField(auto_now_add=True)


