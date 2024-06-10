from django.db import models


# Create your models here.
# db에 저장될 table 생성
class Member(models.Model):
  # max_length = bite단위
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  profile = models.TextField()
  create_date = models.DateTimeField()
# model 작성후 mysite/config/settings에 app 등록