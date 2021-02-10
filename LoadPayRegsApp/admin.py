from django.contrib import admin

from .models import DocFile, TableAndUrlColumns

# Register your models here:
admin.site.register(DocFile)
admin.site.register(TableAndUrlColumns)