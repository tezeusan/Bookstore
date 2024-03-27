from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='avatar')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "users"
        verbose_name_plural = "user"

        def __str__(self):
            return self.username
