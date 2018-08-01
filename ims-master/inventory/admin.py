from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

#admin.site.register(Product)

@admin.register(Product)
class ViewAdmin(ImportExportModelAdmin):
    pass
