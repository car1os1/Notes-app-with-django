from distutils import text_file
from pyexpat import model
from django.db import models

# Create your models here.
class tasks(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(blank=True)