from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomUserCreationForm, UserDetailsForm, UploadFileForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .file_handlers import handle_student_csv, handle_alumni_csv
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import account_activation_token
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

def register(request):
    if request.method == "POST":
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            # user, created = User.objects.get_or_create(
            # email=request.POST.get("email")
            # )
            # domain = get_current_site(request).domain
            # uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            # myurl = 'http://'+domain+link
            # message = 'Hi ' + user.username + ' ' + myurl
            # email = EmailMessage(
            #     "Confirmation",
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     [f.cleaned_data.get('email')],
            # )
            # email.fail_silently = False
            # email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('login')
    else:
        f = CustomUserCreationForm()

    return render(request, "base/register.html", {"form": f})

def activate_account(request):
    return render(request, 'base/activate_account.html')

def log_out(request):
    logout(request)
    return redirect("home")

class IPView(TemplateView):
    template_name = 'base/insufficient_permission.html'


def not_logged_in_error(request):
    return render(request, 'not_logged_in_error.html')

def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'base/activate_success.html')
    else:
        return HttpResponse("Activation link is invalid!")
