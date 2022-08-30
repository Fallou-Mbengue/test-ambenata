# project.models.py

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls.base import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from page.models import BaseTimeStampedModel

from user.models import CustomUser

NULL_AND_BLANK = {'null': True, 'blank': True}


class Category(BaseTimeStampedModel):

    title = models.CharField(
        verbose_name="category title",
        max_length=20
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Project(BaseTimeStampedModel):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.PROTECT,
        verbose_name="project owner",
    )
    category = models.ForeignKey(
        to="project.Category",
        on_delete=models.SET_NULL,
        verbose_name="Categorie",
        null=True,
    )
    title = models.CharField(
        verbose_name="project name",
        max_length=180, null=True,
        help_text="define your project name."
    )
    budget = models.DecimalField(
        verbose_name="project budget",
        decimal_places=2,
        max_digits=12,
        help_text="define the budget for financing your project."
    )
    resume = models.TextField(
        verbose_name="project summary",
        max_length=250, null=True,
        help_text="make an overall summary of your project"
    )
    description = models.TextField(
        verbose_name="project description",
        null=True,
        help_text="make an overall summary of your project"
    )
    logo = models.ImageField(
        verbose_name="project logo",
        upload_to="projects/logo/%Y/%m%d",
        **NULL_AND_BLANK
    )
    video = models.URLField(
        default="https://example.com/URLG5433",
        **NULL_AND_BLANK

    )
    document = models.FileField(
        upload_to="projects/docs/%Y/%m%d",
        validators=[
            FileExtensionValidator(['pdf'])
        ],
        **NULL_AND_BLANK
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="published"
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_offer_update_url(self):
        return reverse(
            "dashboard:project_owner_update_project",
            kwargs={"pk": self.id}
        )

    def get_offer_delete_url(self):
        return reverse(
            "dashboard:project_owner_delete_project",
            kwargs={"pk": self.id}
        )


class FollowedProject(BaseTimeStampedModel):
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
    )
    investor = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
