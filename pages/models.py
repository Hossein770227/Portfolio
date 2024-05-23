from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from django.utils import timezone


class RecevieMessage(models.Model):
    full_name = models.CharField(_("full name"), max_length=150)
    email = models.EmailField(_("email"), max_length=254)
    message = models.TextField(_("message"))
    date_time_create = models.DateTimeField(_("date time created"),auto_now_add=timezone.now())

    class Meta:
        verbose_name = _('RecevieMessage')
        verbose_name_plural = _('RecevieMessage')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("pages:home")
    

class Skills(models.Model):
    name = models.CharField(_("name of course"), max_length=100)
    course = models.CharField(_("course"),max_length=150)
    description = models.TextField(_("description"), blank=True)
    date_time_create = models.DateTimeField(_('date time created'),auto_now_add=timezone.now())
    active = models.BooleanField(_("active"),default=True)

    class Meta:
        verbose_name = _('skills')
        verbose_name_plural = _('skills')

    def __str__(self):
        return f'{self.name} {self.course}'
    
class Portfolio(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='cover/', )
    date_time_created = models.DateTimeField(_("date time create"), auto_now_add=True)
    active = models.BooleanField(_("active"),default=True)

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')