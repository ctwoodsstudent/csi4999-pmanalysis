from django.contrib import admin
from .models import UserFiles, GEOStudy, Report, UserGEO
# Register your models here.

admin.site.register(UserFiles)
admin.site.register(GEOStudy)
admin.site.register(Report)
admin.site.register(UserGEO)
