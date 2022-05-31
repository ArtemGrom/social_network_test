from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_add',)

    def __str__(self):
        return self.title
