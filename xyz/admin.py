from django.contrib import admin
from .models import *


admin.site.register(Suspect)
admin.site.register(Victim)
admin.site.register(TheftCase)
admin.site.register(StolenItem)
admin.site.register(History)
admin.site.register(Notification)
admin.site.register(PoliceCenter)
admin.site.register(PoliceOfficer)
admin.site.register(InvestigationReport)
admin.site.register(Evidence)
admin.site.register(Witness)



# Register your models here.
