# myapp/models.py
from django.db import models


class User(models.Model):
    DoesNotExist = None
    objects = None
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = ''  # Add this line to specify the app_label
        db_table = 'user'
