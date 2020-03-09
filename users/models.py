from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    
user_name = models.CharField(max_length=50)
email = models.EmailField(max_length=100)
password = models.CharField(max_length=40)
image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


def __str__(self):
    return self.user_name


class Snippet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    code = models.