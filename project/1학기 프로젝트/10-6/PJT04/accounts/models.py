from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Django 가 기본적으로 user 모델을
# 왜 덮어써야 하는가?
# 1. Django 권장사항
# 2. 커스텀을 하기 위해서
class User(AbstractUser):
    # 내가 원하는 추가적인 필드를 사용
    nickname = models.CharField(max_length=30)