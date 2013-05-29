from django.core.urlresolvers import reverse
from django.db import models
from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(TinyMCE(attrs={'cols': 80, 'rows': 80}))
    mas = models.TextField(TinyMCE(attrs={'cols': 80, 'rows': 80}))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.TextField(TinyMCE(attrs={'cols': 80, 'rows': 80}))
