from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    title = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=timezone.now)
    likes = GenericRelation(Like)

    class Meta:
        ordering = ('-date_add',)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
