from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class Student(models.Model):
    class Meta:
        db_table = 'students'
    
    usn = models.CharField(max_length=10)
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50,validators=[RegexValidator('[+-/%@$^&*()!:;]',inverse_match=True)])
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100, unique = True)
    rv_email = models.CharField(max_length=100, unique = True)
    branch = models.CharField(max_length=50)
    year_joined = models.DateField()

class skills(models.Model):
    stud=models.ForeignKey(Student,on_delete=models.CASCADE ,related_name='skills',default=None,blank=True,null=True)
    skill=models.CharField(max_length=50)

    class Meta:
        db_table = 'skills'
