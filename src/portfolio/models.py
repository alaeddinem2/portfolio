from django.db import models
from django.db.models.fields import CharField
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

from django_resized import ResizedImageField
# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=100,null=True,verbose_name=_("Name"),blank=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("Category"))
    slug=models.SlugField(verbose_name=_("Slug"),blank=True)
    description=models.TextField(blank=True)
    client=models.ForeignKey('Client',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("Client"))
    start_date=models.DateField(verbose_name=_("Start Date "),blank=True)
    end_date=models.DateField(verbose_name=_("End Date "),blank=True)
    live_demo_url=models.CharField(max_length=100,verbose_name=_("live demo  "),blank=True)
    github_url=models.CharField(max_length=100,verbose_name=_("github  "),blank=True)
    image = models.ImageField(upload_to="projects/")

    
    

    def __str__(self) :
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name+'-'+str(self.client))
        super(Project,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

  
    def get_absolute_url(self):
        return reverse("portfolio:project_detail", kwargs={"slug": self.slug})

class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name=_("Name"))

    def __str__(self) :
        return self.name

    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Client(models.Model):
    name=models.CharField(max_length=50,verbose_name=_("Name"))

    def __str__(self) :
        return self.name

    
    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("Clients")


class ProjectImage(models.Model):
    images=models.ImageField(upload_to="projects/",verbose_name=_("Images"),blank=True)
    project=models.ForeignKey('Project',on_delete=models.CASCADE)


    def __str__(self) :
        return self.project.name +"_img"
    
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img=Image.open(self.images.path)
    #     if img.width !=850 or img.height !=400:
    #         img.thumbnail((850,400)) 
    #         img.save(self.images.path)

    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self) :
        return "message from: " + self.name
 

    