from django.contrib import admin

from . import models as md


admin.site.register(md.Cinema)
admin.site.register(md.Hall)
admin.site.register(md.Row)
admin.site.register(md.Seat)
admin.site.register(md.Session)
