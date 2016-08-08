from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    # @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })