from django.db import models
# 어떻게 클래스처럼 . 으로 접근할 수 있을까?
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass