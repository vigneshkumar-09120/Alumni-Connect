from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def switch_view(admin, alumni, student):
    def switch(request):
        if request.user.has_perm('auth.is_admin'):
            return admin(request)
        elif request.user.has_perm('auth.is_alumnus'):
            return alumni(request)
        else:
            return student(request)
    return switch