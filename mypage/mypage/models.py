import uuid

from django.db import models
from django.contrib.auth.models import User


def get_uid(limit):
    return str(uuid.uuid4())[:limit]


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)


class Blog(models.Model):
    uid = models.CharField(unique=True, max_length=20, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, default='')
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    PRIVATE, PUBLIC = range(2)

    PRIVACY_CHOICES = [(PUBLIC, 'Public'), (PRIVATE, 'Private')]
    privacy = models.IntegerField(choices=PRIVACY_CHOICES, default=PRIVATE)

    # This will be called every time a blog is modified in the database.
    def save(self, *args, **kwargs):
        self.uid = self.uid or get_uid(5)

        super(Blog, self).save(*args, **kwargs)
