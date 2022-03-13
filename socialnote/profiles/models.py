from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    age = models.IntegerField()
    gender=models.IntegerField()
    country_user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class Country(models.Model):
    id_country = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name_country = models.CharField(max_length=100)

