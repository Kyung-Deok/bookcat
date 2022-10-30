from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

class User(models.Model):
    username = models.CharField(db_column='username',max_length=50)
    password = models.CharField(db_column='password', max_length=600)
    fullname = models.CharField(db_column='fullname', max_length=50)
    useremail = models.CharField(db_column='useremail', max_length=50, blank=True)
    # usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='y')
    create_at = models.DateTimeField(db_column='create_at', auto_now_add=True)
    update_at = models.DateTimeField(db_column='update_at', auto_now=True)
    userpick = models.TextField(db_column='usage_flag', default='')

    class Meta:
#       managed = False
        db_table = 'serviceuser'
 
    def __str__(self):
        return '이름 : ' + self.fullname + ", 이메일 : " + self.useremail
    