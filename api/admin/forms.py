from django.core.exceptions import ValidationError

from base.models import Document
from .models import Event
from django.contrib.auth.models import User
from django import forms

class UploadForm(forms.ModelForm):
    def validate_file(file):
        if not file.name.endswith('.xlsx'):
            raise ValidationError("Only csv file format supported!")
        return file

    file = forms.FileField(validators=[validate_file], widget=forms.FileInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Document
        fields = ["name", "file"]

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields= '__all__'
        widgets = {
            'Event_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Event Id (starting from 100)"}),
            'Name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Event Name"}),
            'Image': forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}),
            'Location': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Location"}),
            'Date': forms.DateInput(attrs={"type":'date',"class": "form-control", "placeholder": "select date"}),
            'Time': forms.TimeInput(attrs={"type":'time',"class": "form-control", "placeholder": "select time"}),
            'Description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Event Description"}),
             
        }  