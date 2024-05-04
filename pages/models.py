from django.db import models
from django.utils.translation import gettext_lazy as _

class Information(models.Model):
    CONDITION_CHOICES = (
        ('r', _('ready')),
        ('un', _("unprepared")),
    )
    fist_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=50)
    about_me = models.TextField()

