from django.contrib.auth.models import User
from base.models import Role

import logging
logger = logging.getLogger('app')

def check_if_alumni(user):
    if user.is_anonymous:
        return False
    user = User.objects.get(username=user)
    return Role.objects.get(user=user).is_alumni