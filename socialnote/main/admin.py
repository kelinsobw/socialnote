from django.contrib import admin

from main.models import Databases


@admin.register(Databases)
class DatabasesAdmin(admin.ModelAdmin):
    list_display = ("author", "db_name", "db_description", "privates")
    fields = ("author", "db_name", "db_description", "privates")
    search_fields = ("db_name",)
