from django.conf import settings
from django.db import models


# The class contains possible variants
# of a person's gender. Used when registering a user
class Gender:
    gender_choice = [
            ("m", 'Male'),
            ("f", 'Female')]


# The class contains possible variants of the
# countries of residence. Used when registering a user
class Country:
    country_choice = [
            ("by", 'Belarus'),
            ("ru", 'Russia')]

# Additional information about the user during registration
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user_image = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=40, choices=Country.country_choice)
    gender = models.CharField(max_length=40, choices=Gender.gender_choice)

