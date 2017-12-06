from django.db import models


class AwardNominee(models.Model):
    skitname = models.CharField(max_length=30)
    nomineedescription = models.CharField(max_length=30)
    nomineepic = models.ImageField()
    votecount = models.IntegerField()
