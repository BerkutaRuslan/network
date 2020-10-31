from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.phone
