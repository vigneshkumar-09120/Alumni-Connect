from django.contrib.auth.models import User
from .models import Document
from student.models import Student
from alumni.models import Alumni
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class CustomUserCreationForm(UserCreationForm):
    def validate_email(email):
        # if (User.objects.get(email=email).is_active):
        #     raise ValidationError("Account already exists.")
        if not (Student.objects.filter(email=email).exists() or Alumni.objects.filter(email=email).exists()):
            raise ValidationError("Email not recognized. Contact the admin.")
        return email

    username = forms.CharField(
        label="Enter Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
    )
    email = forms.EmailField(
        validators=[validate_email],
        label="Enter email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )
    password1 = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm your password"}
        ),
    )

    def save(self):
        user = User.objects.get(
            email=self.cleaned_data["email"]
        )
        
        # role, created = Role.objects.get_or_create(
        #     user=user, is_student = True
        # )
        # user.is_active = False
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        )
    )

class UploadFileForm(forms.ModelForm):
    def validate_file(file):
        if not file.name.endswith('.csv'):
            raise ValidationError("Only csv file format supported!")
        return file
    file = forms.FileField(validators=[validate_file], widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta:
        model = Document
        fields = (
            "name",
            "file",
        )


class UserDetailsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(UserDetailsForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="Username", min_length=4, max_length=150)
    email = forms.EmailField(label="Email")

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        r = User.objects.filter(username=username).exclude(pk=self.user.id)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        r = User.objects.filter(email=email).exclude(pk=self.user.id)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        obj, created = User.objects.get_or_create(username=self.user.username)
        obj.username = self.cleaned_data["username"]
        obj.email = self.cleaned_data["email"]
        obj.save()
        return obj
