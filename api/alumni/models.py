from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
category_choices = (
    ("Enterprenuer","Enterprenuer"),
    ("Higher Studies","Higher Studies"),
    ("Job","Job"),
    ("Others","Others"),

)
role_choices = (
    ("Consultancy","Consultancy"),
    ("Finanace","Finanace"),
    ("Software Developer","Software Developer"),
    ("Data Analyst","Data Analyst"),
    ("Network Security","Network Security"),
    ("Cloud Computing ","Cloud Computing"),
    ("IT project management","IT project management"),
    ("AI and ML","AI and ML"),
    ('others','others')
)

role_choices = (
    ("Consultancy","Consultancy"),
    ("Finance","Finance"),
    ("Software Developer","Software Developer"),
    ("Data Analyst","Data Analyst"),
    ("Network Security","Network Security"),
    ("Cloud Computing","Cloud Computing"),
    ("IT project management","IT project management"),
    ("AI and ML","AI and ML"),
    ('others','others')
)

spe_choices = (
    ("Artificial Intelligence","Artificial Intelligence"),
    ("Machine Learning","Machine Learning"),
    ("Cloud Computing","Cloud Computing"),
    ("Data Science","Data Science"),
    ("Computer Vision","Computer Vision"),
    ("Natural Language processing","Natural Language processing"),
    ("Marketing","Marketing"),
    ("Finance Systems","Finanace Systems"),
    ("IOT","IOT"),
    
    ('others','others'),
)
degree_choices=(
  ("M Tech","M Tech"),
    ("MSc","MSc"),
    ("MBA","MBA"),
    ("Others","Others"),  
)
class Alumni(models.Model):
    
    usn = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alumnus_details')
    name = models.CharField(max_length=100, null=True,validators=[RegexValidator('[+-/%@$^&*()!:;]',inverse_match=True)])
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    rv_email = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=50, null=True)
    year_joined = models.DateField(null = True)
    year_passed = models.DateField(null = True)

    class Meta:
        db_table = 'alumni'

class Category(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE,null=True,blank=True)
    Category=models.CharField(max_length=20,choices=category_choices,default='Job')
    description=models.CharField(max_length=250,null=True,blank=True)
    

    class Meta:
        db_table = 'category'

class Job(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE,null=True,blank=True)
    
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, null=True,choices=role_choices)
    salary = models.FloatField(max_length=20, null=True,blank=True)
    location=models.CharField(max_length=20)
    

    class Meta:
        db_table = 'job'


class Higherstudies(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE,null=True,blank=True)
    college_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True,choices=spe_choices)
    degree = models.CharField(max_length=20, null=True,choices=degree_choices)
    location=models.CharField(max_length=20,null=True)
    yearofgrad = models.DateField(max_length=10, null=True)
    

    class Meta:
        db_table = 'higherstudies'




    