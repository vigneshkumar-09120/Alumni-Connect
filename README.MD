###### Run Docker command to initially start the project.

```Shell
docker-compose up
```
###### New terminal to run commands.

```Shell
docker exec -it dbdex_api_c bash
```
###### Run migrations to migrate tables to database.

```Shell
python manage.py makemigrations
python manage.py migrate
```

###### To run python code.

```Shell
python manage.py shell
```

###### To create groups for Admins and create one Admin.

```Python
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

admins, _ = Group.objects.get_or_create(name='admins')
admins_ct = ContentType.objects.get(app_label='auth', model='user')
is_admin, _ = Permission.objects.get_or_create(name='is_admin', codename='is_admin', content_type=admins_ct)
admins.permissions.add(is_admin)
is_admin.save()
admin,_ = User.objects.get_or_create(username='admin')
admin.set_password('anteater')
admin.groups.add(admins)
admin.save()
admin.has_perm('auth.is_admin')
```

###### To create groups for Alumni.

```Python
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
alumni, _ = Group.objects.get_or_create(name='alumni')
alumni_ct, _ = ContentType.objects.get_or_create(app_label='auth', model='user')
is_alumnus, _ = Permission.objects.get_or_create(name='is_alumnus', codename='is_alumnus', content_type=alumni_ct)
alumni.permissions.add(is_alumnus)
```

###### To create groups for Students.

```Python
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
students, _ = Group.objects.get_or_create(name='students')
students_ct, _ = ContentType.objects.get_or_create(app_label='auth', model='User')
is_student, _ = Permission.objects.get_or_create(name='is_student', codename='is_student', content_type=students_ct)
students.permissions.add(is_student)
```
###### To delete a particular user.
```Python
from django.contrib.auth.models import User
User.objects.get(username='<username>').delete()
```