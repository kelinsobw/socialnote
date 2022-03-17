from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "gender", "user_image", "country")
    fields = ("user", "age", "gender", "user_image", "country")
    readonly_fields = ("created_at",)
    search_fields = ("user__email",)
    raw_id_fields = ("user",)
