from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

class MyUser(AbstractBaseUser):
    first_name= models.CharField(verbose_name=_('first name'), max_length=100)
    last_name= models.CharField(verbose_name=_('last name'), max_length=100)
    phone_number =  models.CharField(verbose_name=_('phone number'), max_length=11, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)



    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS =['first_name', 'last_name']
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superuser(self):
        return True
