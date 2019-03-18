from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class HashTag(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

class Link_Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_url = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    comments = models.ManyToManyField('Comment')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('link_post-detail', args=[str(self.id)])

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ManyToManyField(Link_Post)
    voted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = models.TextField(max_length=255)
    post = models.ManyToManyField(Link_Post)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return f'{self.id} ({self.link_post.title})'

