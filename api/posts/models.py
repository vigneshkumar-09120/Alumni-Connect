from django.db import models
from django.apps import apps
from django.urls import reverse

from alumni.models import Alumni

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'posts'
    