

from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password):

        if not phone_number:
            raise ValueError("user must have phone number")
        user = self.model(phone_number=phone_number, )
        user.set_password((password))
        user.save(using=self._db)
        return user

    def create_superuser(self,  phone_number,  password):
        user = self.create_user( phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
