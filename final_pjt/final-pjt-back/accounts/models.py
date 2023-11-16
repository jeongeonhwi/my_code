from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    hate = models.ManyToManyField('self', symmetrical=False, related_name='hated')
    like = models.ManyToManyField('self', symmetrical=False, related_name='liked')
    
    def __str__(self) :
        return self.username