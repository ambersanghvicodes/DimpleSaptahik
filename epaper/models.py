from django.db import models
import os
# Create your models here.

def upload_to_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.id, ext)
    return os.path.join('media/{}'.format(instance.id), filename)

class EPaper(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField(default=None)
  pdf = models.FileField(upload_to='media/epaper',default='',blank=True,null=True)
  image = models.ImageField(upload_to='media/epaper/images',default='',blank=True,null=True)

  def __str__(self):
       return self.name