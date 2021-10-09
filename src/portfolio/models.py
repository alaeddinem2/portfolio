from django.db import models
from django.db.models.fields import CharField
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class Visit(models.Model):
    visitor_name=models.CharField(max_length=20)
    visitor_ip=models.CharField(max_length=20)
    time=models.CharField(max_length=19)

    def __str__(self) :
        return str(self.id)
class Project(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("author"))
    name=models.CharField(max_length=100,null=True,verbose_name=_("Name"),blank=True,default="Embedded Systems")
    category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("Category"),default="")
    slug=models.SlugField(verbose_name=_("Slug"),blank=True)
    description=models.TextField(blank=True,default="this ")
    client=models.ForeignKey('Client',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("Client"))
    start_date=models.DateField(verbose_name=_("Start Date "),blank=True,null=True)
    end_date=models.DateField(verbose_name=_("End Date "),blank=True,null=True)
    live_demo_url=models.CharField(max_length=100,verbose_name=_("live demo  "),blank=True,null=True)
    github_url=models.CharField(max_length=100,verbose_name=_("github  "),blank=True,null=True)
    image = models.ImageField(upload_to="projects/",blank=True,null=True)

    
    

    def __str__(self) :
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name +'-'+ str(self.client))
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
 
def create_project(sender,**kwargs):
    if kwargs['created']:
        project= Project.objects.create(author=kwargs['instance'])

post_save.connect(create_project,sender=User)
    