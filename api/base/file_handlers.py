from django.forms import ValidationError
import pandas as pd
from datetime import datetime
from django.contrib.auth.models import User, Group
from alumni.models import Alumni
from student.models import Student

def handle_student_csv(file):
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        usn = row['USN']
        
        name = row['FULL NAME']
        phone = row['PHONE']
        rv_email = row['RVCE Mail ID']
        email = row['EMAIL']
        
        branch = row['BRANCH']
        year_joined = row['YEAR JOIN']
        
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.username = email[:len(email)-12]
            user.set_password('anteater')
            user.save()
            group = Group.objects.get(name='students')
            group.user_set.add(user)
            obj, created = Student.objects.get_or_create(
                usn=usn,  name=name, phone=phone, rv_email=rv_email, email=email, year_joined=year_joined, branch=branch, user=user)

def handle_alumni_csv(file):
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        usn = row['USN']
        name = row['Name']
        phone = row['Phone']
        email = row['RV Email']
        year = email[len(email)-14:len(email)-12]
        branch = row['Department']
        year_joined = datetime.strptime(year, '%y').date()
        year_passed = datetime.strptime(str(year + 4), '%Y')
        personal_email = row['Personal Email']
        company_name = row['Company Name']
        ctc = row['CTC']
        type = row['Type']
        job_profile = row['Job Profile']
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.username = email[:len(email)-12]
            user.set_password('anteater')
            user.save()
            group = Group.objects.get(name='alumni')
            group.user_set.add(user)
            obj, created = Alumni.objects.get_or_create(
                usn=usn, name=name, phone=phone, email=email, personal_email=personal_email, job_profile=job_profile, type=type, ctc=ctc, company_name=company_name, year_joined=year_joined, year_passed=year_passed, branch=branch, user=user)
