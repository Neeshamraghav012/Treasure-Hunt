from django.contrib import admin
from .models import Team, Questions, Entries

# Register your models here.
admin.site.register(Team)
admin.site.register(Questions)
admin.site.register(Entries)