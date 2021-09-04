from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    def __str__(self):
        return f'{self.user.username} Profile'

