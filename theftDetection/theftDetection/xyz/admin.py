from django.contrib import admin
from .models import *

admin.site.register(Victim)
admin.site.register(PoliceOfficer)
admin.site.register(TheftCase)
admin.site.register(StolenItem)
admin.site.register(Witness)
admin.site.register(Evidence)
admin.site.register(InvestigationReport)
admin.site.register(Notification)
admin.site.register(History)