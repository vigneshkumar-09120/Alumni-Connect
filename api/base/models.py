from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'documents'

