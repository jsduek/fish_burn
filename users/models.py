from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from common.models import Common

class User(AbstractBaseUser, Common):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    class Meta:
        db_table="users"

