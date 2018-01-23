from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe

from markdown import markdown


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    subject = models.CharField(max_length=255)
    detail = models.CharField(max_length=2000)
    author = models.ForeignKey(User, related_name='posts')
    categories = models.ManyToManyField(Category, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-updated_at', '-published_at', 'subject',)

    @property
    def detail_markdown(self):
        return mark_safe(markdown(self.detail, safe_mode='escape'))

    def __str__(self):
        return self.subject


class Comment(models.Model):
    message = models.CharField(max_length=1500)
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User, related_name='comments')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-published_at',)

    @property
    def message_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

    def __str__(self):
        return '{} ({})'.format(self.message[slice(40)], self.post.subject)
