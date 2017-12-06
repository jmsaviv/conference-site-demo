from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from workshops.models import Workshops

def workshopschedule(request):
    workshops = Workshops.objects.all()
    return render(request, 'workshopschedule.html', {'workshops': workshops})


