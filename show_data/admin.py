from django.contrib import admin

from . import models as md


admin.site.register(md.Movie)
admin.site.register(md.Genre)
admin.site.register(md.Collection)