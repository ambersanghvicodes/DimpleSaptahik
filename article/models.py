from django.db import models
from datetime import datetime
import os

def upload_to_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.id, ext)
    return os.path.join('media/{}'.format(instance.id), filename)

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  designation = models.CharField(max_length=50,default='')
  
  def __str__(self):
       return self.name


class ArticleImage(models.Model):
    article = models.ForeignKey('Article', related_name='article_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/article_images', default='', blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to=upload_to_path, null=True, blank=True)

    def __str__(self):
       return self.title
    
    @property
    def author_name(self):
        return self.author.name