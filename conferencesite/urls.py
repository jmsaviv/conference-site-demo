"""conferencesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from registrant import views as registrantviews
from awardnominee import views as awardnomineeviews
from workshops import views as workshopsviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^activities$', views.activities, name='activities'),
    url(r'^funstufftodo$', views.activities, name='activities'),
    url(r'^registration$', registrantviews.get_name, name="registration"),
    url(r'^thankyou$', registrantviews.get_name, name='thankyou'),
    url(r'^meals', views.meals, name='meals'),
    url(r'^keynote', views.keynote, name='keynote'),
    url(r'^workshopschedule', workshopsviews.workshopschedule, name='workshopschedule'),
    url(r'^awards', awardnomineeviews.awards, name='awards'),
    url(r'^admin/', admin.site.urls)
]
