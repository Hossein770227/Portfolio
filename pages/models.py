from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 


class RecevieMessage(models.Model):
    full_name = models.CharField(_("full name"), max_length=150)
    email = models.EmailField(_("email"), max_length=254)
    message = models.TextField(_("message"))
    date_time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("pages:home")
    

class Skills(models.Model):
    name = models.CharField( max_length=100)
    course = models.CharField(max_length=150)
    description = models.TextField()
    date_time_create = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.course}'