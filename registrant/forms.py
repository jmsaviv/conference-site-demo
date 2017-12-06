from django.forms import ModelForm
from registrant.models import Registrant
from django import forms

TITLE_CHOICES = ('Dr.', 'Ms.', 'Mr.')

MEAL_CHOICES = ('mealpack', 'dinnerday2')

SESSION_1_CHOICES = ('Workshop A', 'Workshop B', 'Workshop C')

SESSION_2_CHOICES = ('Workshop D', 'Workshop E', 'Workshop F')

SESSION_3_CHOICES = ('Workshop G', 'Workshop H', 'Workshop I')

CREDIT_CARD_CHOICES = ('AE', 'MC', 'V')


class RegistrationForm(ModelForm):
    class Meta:
        model = Registrant
        fields = [
            'title',
            'firstname',
            'lastname',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'telephone',
            'email',
            'website',
            'position',
            'company',
            'meals',
            'billing_firstname',
            'billing_lastname',
            'card_type',
            'card_csv',
            'exp_year',
            'exp_month',
            'session1',
            'session2',
            'session3'#,
            #'date_of_registration'
        ]
    #widgets = {'title': forms.Select(choices=TITLE_CHOICES)}







