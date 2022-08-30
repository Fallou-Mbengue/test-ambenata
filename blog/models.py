# blog.models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

import readtime
from taggit.managers import TaggableManager


from blog.managers import PostManager
from page.models import BaseTimeStampedModel

NULL_AND_BLANK = {'null': True, 'blank': True}


class Post(BaseTimeStampedModel, models.Model):
    title = models.CharField(
        verbose_name="title",
        max_length=255,
        help_text='add title for article'
    )
    subtitle = models.CharField(
        verbose_name="subtitle",
        max_length=255, blank=True,
        help_text='add subtitle for article'
    )
    body = models.TextField(verbose_name="content")
    image = models.ImageField(
        verbose_name="post cover",
        upload_to="blog/"
    )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        verbose_name="author"
    )
    slug = models.SlugField(
        verbose_name="slug",
        unique=True,
        **NULL_AND_BLANK
    )
    published = models.BooleanField(
        verbose_name="published",
        default=False
    )
    tags = TaggableManager(verbose_name="keywords")

    objects = PostManager()

    class Meta:
        ordering = ["-created"]
        get_latest_by = ['-created']
        verbose_name_plural = 'blog'
        indexes = [
            models.Index(fields=['id']),
        ]

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_readtime(self):
        read_time_post = readtime.of_text(self.body)
        return read_time_post

    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"slug": str(self.slug)})
