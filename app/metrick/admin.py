from django.contrib import admin
from .models import VisitLog

class VisitLogAdmin(admin.ModelAdmin):
    list_display = ("session_id", "action")
    list_filter = ("action",)

admin.site.register(VisitLog, VisitLogAdmin)
