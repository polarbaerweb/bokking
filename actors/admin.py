from django.contrib import admin

from . import models as md

admin.site.register(md.Actors)
admin.site.register(md.Prizes)
admin.site.register(md.Jobs)