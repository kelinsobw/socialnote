from django.contrib import admin

from main.models import Databases


@admin.register(Databases)
class DatabasesAdmin(admin.ModelAdmin):
    list_display = ("author", "db_name", "db_description", "created_at")
    fields = ("author", "db_name", "db_description", "created_at")
    readonly_fields = ("created_at",)

