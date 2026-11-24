from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class news(models.Model):
    title=models.CharField(max_length=200)
    des=HTMLField()
    
    
    

    def __str__(self):
        return self.title

   