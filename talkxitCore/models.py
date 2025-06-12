from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    name=models.CharField(max_length=144)
    surname=models.CharField(max_length=144)
    birthday=models.DateField()
    avatar=models.ImageField(blank=True,null=True)
    REQUIRED_FIELDS=['name','surname','birthday']