from django.contrib import admin
from workshops.models import Workshops


class WorkshopsAdmin(admin.ModelAdmin):
    list_display = ('session', 'name', 'roomnumber', 'starttime',
                    'endtime')
    list_filter = ('session', 'name', 'roomnumber', 'starttime',
                    'endtime')

admin.site.register(Workshops, WorkshopsAdmin)
