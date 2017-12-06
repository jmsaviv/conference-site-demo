import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conferencesite.settings'
django.setup()


from django.core.management.base import BaseCommand
from registrant.models import Registrant


class Command(BaseCommand):
    help = 'Loads the project with registrant data.'

    def handle(self, *args, **options):

        person1 = Registrant(
            title = "Ms.",
            firstname = "Jill",
            lastname = "Jackson",
            address1 = "123 Main St",
            address2 = "Apt. 183",
            city = "Denver",
            state = "CO",
            zipcode = "80302",
            telephone = "303-123-4567",
            email = "jill@fake.com",
            website = "http://www.regis.edu",
            position = "Web Developer",
            company = "Regis University",
            meals = "mealpack",
            billing_firstname = "Jill",
            billing_lastname = "Jackson",
            card_type = "MC",
            card_number = "1234567891234560",
            card_csv = "5594",
            exp_year = "2016",
            exp_month = "12",
            session1 = "Workshop A",
            session2 = "Workshop D",
            session3 = "Workshop G",
            date_of_registration = "2016-06-17"
        )

        person1.save()
