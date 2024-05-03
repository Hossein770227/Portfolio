

from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, first_name,last_name,phone_number, password):
        if not first_name:
            raise ValueError("user must have first name")
        if not last_name:
            raise ValueError("user must have last name")
        if not phone_number:
            raise ValueError("user must have phone number")
        user = self.model(first_name=first_name,last_name=last_name,phone_number=phone_number, )
        user.set_password((password))
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number,  password):
        user = self.create_user(first_name, last_name, phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
