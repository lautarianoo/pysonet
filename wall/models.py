from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from comments.models import AbstractComment
from profiles.models import UserNet
from django.conf import settings

class Post(models.Model):
    '''Post model'''

    text = models.TextField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.user} - {self.create_date}'

    def comments_count(self):
        return self.comments.count()

class Comment(AbstractComment, MPTTModel):
    '''Модель комментариев к постам'''

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)