from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(default ='default.jpeg', null=True, blank=True)
    contact = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return "Profile of User {}".format(self.user.username)
