from django.db import models
from django.db.models.fields import SlugField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
import datetime

# Create your models here.


class Profile(models.Model):
    ProUser=models.OneToOneField(User, verbose_name=_("User "), on_delete=models.CASCADE)
    ProSlug=models.SlugField(verbose_name=_("Slug"),blank=True,null=True)
    ProImage=models.ImageField(upload_to="profile_pics",default='default.jpg',verbose_name=_("Profile Image"),blank=True, null=True)
    ProCountry=CountryField(verbose_name=_("Country "))
    ProAddress=models.CharField(verbose_name=_("Address"),max_length=100,blank=True, null=True)
    ProJoin_date=models.DateTimeField(verbose_name=_("join date"),default=datetime.datetime.now)

    def __str__(self):
        return  '%s' %(self.ProUser)

    def save(self, *args, **kwargs):
        if not self.ProSlug:
            self.ProSlug=slugify(self.ProUser.username)
        super(Profile,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def get_absolute_url(self):
        return reverse("accounts:profile_detail", kwargs={"slug": self.ProSlug})

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(ProUser=kwargs['instance'])


post_save.connect(create_profile,sender=User)