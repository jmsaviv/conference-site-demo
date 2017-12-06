from django.db import models


class Workshops(models.Model):

    name = models.CharField(max_length=30)
    session = models.IntegerField()
    roomnumber = models.CharField(max_length=10)
    starttime = models.CharField(max_length=5)
    endtime = models.CharField(max_length=5)
