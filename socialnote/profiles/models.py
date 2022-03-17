from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField(null=True, blank=True)
    gender_choice = [
        ("M", 'Male'),
        ("F", 'Female')]
    gender = models.CharField(max_length=1, choices=gender_choice)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user_image = models.ImageField(null=True, blank=True)
    country_choice = [
        ("by", 'Belarus'),
        ("ru", 'Russia')]
    country = models.CharField(max_length=40, choices=country_choice)
