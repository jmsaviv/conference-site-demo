import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conferencesite.settings'
django.setup()

from django.core.management.base import BaseCommand
from workshops.models import Workshops


class Command(BaseCommand):
    help = 'Loads the project with workshop data.'

    def handle(self, *args, **options):

        workshop = Workshops(
            name="Comedy Writing",
            session=1,
            roomnumber="A203",
            starttime="9 AM",
            endtime="12 PM"

        )

        workshop.save()






