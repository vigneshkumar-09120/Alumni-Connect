from django.db import models
from django.apps import apps
from django.contrib.auth.models import User

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.posted_by)

    class Meta:
        db_table = 'comments'