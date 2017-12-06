import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'conferencesite.settings'
django.setup()


from django.core.management.base import BaseCommand
from awardnominee.models import AwardNominee


class Command(BaseCommand):
    help = 'Loads the project with award data.'

    def handle(self, *args, **options):

        nominee2 = AwardNominee(
            skitname="Player Hater's Ball",
            nomineedescription="Hater's gonna hate",
            nomineepic="static/images/playerhater.jpeg",
            votecount=5

        )

        nominee2.save()