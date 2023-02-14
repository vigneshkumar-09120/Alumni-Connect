from django.core.exceptions import ValidationError

from .models import Student,skills
from base.models import Document

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms


class StudentCreationForm(forms.ModelForm):

    def clean_user(self):
        email = self.cleaned_data['email']
        user, _ = User.objects.get_or_create(email=email)
        students = Group.objects.get(name='students')
        user.username = email[:len(email)-12]
        user.set_password('anteater')
        user.groups.add(students)
        user.save()
        return user

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Student
        fields = ['name', 'usn', 'phone', 'rv_email',
                  'email', 'branch', 'year_joined', 'user']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the name"}),
            'usn': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the USN"}),
            
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the phone number"}),
            'rv_email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the RV email"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter the email"}),
            'branch': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the branch"}),
            'year_joined': forms.DateInput(attrs={'type': 'date',"class": "form-control"})
        }


class StudentUploadForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.csv'):
            raise ValidationError(
                "Only csv file format supported!", code='invalid')
        return file

    class Meta:
        model = Document
        fields = (
            "name",
            "file",
        )
        widgets = {'file': forms.FileInput(attrs={"class": "form-control"})}

class skillform(forms.ModelForm):
    class Meta:
        model=skills
        fields= '__all__'
        widgets = {
            'skill': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the skill"}),
        }