from django.db import models
from django.utils.translation import gettext_lazy as _ 


class RecevieMessage(models.Model):
    email = models.EmailField(_("email"), max_length=254)
    message = models.TextField(_("message"))

    def __str__(self):
        return self.email