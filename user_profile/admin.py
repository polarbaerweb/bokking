from django.contrib import admin

from . import models as user_md

# Register your models here.
admin.site.register(user_md.Booking)
admin.site.register(user_md.Ticket)