from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , related_name="user" , on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True , null=True)
    description = models.TextField(max_length=200, blank=True , null=True)
    subtitle = models.CharField(max_length=30, blank=True , null=True)
    job_name = models.CharField(max_length=30, blank=True , null=True)
    image = models.ImageField(upload_to='profile/', blank=True , null=True)
    address = models.CharField(max_length=30, blank=True , null=True)
    provenece = models.CharField(max_length=30, blank=True , null=True)
    working_hour = models.IntegerField( blank=True , null=True)
    number = models.CharField(max_length=20, blank=True , null=True)
    price = models.IntegerField( blank=True , null=True)
    slug = models.SlugField(max_length=30, blank=True , null=True)
    working_time = models.IntegerField( blank=True , null=True)
    department = models.CharField(max_length=30 , null=True , blank=True)

    def __str__(self):
        return str(self.user.username)
    
def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Profile, self).save(*args, **kwargs)
        


def create_profile(sender , created , instance ,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)