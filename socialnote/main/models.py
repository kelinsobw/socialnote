from django.conf import settings
from django.db import models


# This table contains data about all the user's tables.
class Databases(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="database"
    )
    db_name = models.CharField(unique=True, max_length=30)
    db_description = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

# This table contains data about database privacy.
class Privates(models.Model):
    base = models.ForeignKey(Databases, on_delete=models.CASCADE)
    privates = models.CharField(max_length=10)
