from django.db import models
from django.utils.translation import gettext_lazy as _ 


class RecevieMessage(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)

    email = models.EmailField(_("email"), max_length=254)
    message = models.TextField(_("message"))
    date_time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email