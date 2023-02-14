import pandas as pd
from datetime import datetime
from django.contrib.auth.models import User, Group
from alumni.models import Alumni

def handle_alumni_csv(file):
    data = pd.read_csv(file)
    try:
        for _, row in data.iterrows():
            usn = row['USN']
            name = row['Name']
            phone = row['Phone']
            rv_email = row['RV Email']
            email=row['Email']
            branch = row['Department']
            year_joined =row['Year Join']
            year_passed=row['Year Pass']
            
            

            group = Group.objects.get(name='alumni')
            user, _ = User.objects.get_or_create(email = email)
            user.username = email[:len(email)-12]
            user.set_password('anteater')
            user.groups.add(group)
            user.save()

            if Alumni.objects.filter(usn = usn).exists():
                alumnus = Alumni.objects.get(usn=usn)
            else:
                alumnus = Alumni.objects.create(usn = usn, user = user)
            alumnus.user = user
            alumnus.name = name
            alumnus.phone = phone
            alumnus.rv_email = rv_email
            alumnus.email = email
            alumnus.year_joined = year_joined
            alumnus.year_passed = year_passed
            alumnus.branch = branch
            alumnus.save()
            
            
        return True
    except Exception as e:
        print(e)
        return False
