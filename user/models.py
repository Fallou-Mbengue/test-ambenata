# user.models.py

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager


NULL_AND_BLANK = {'null': True, 'blank': True}


class CustomUser(AbstractUser):

    EXPERIENCE_CHOICES = (
        ("-1", "Moins d'une année"),
        ("1-3", "1-3 ans"),
        ("3-5", "3-5 ans"),
        ("5-10", "5-10 ans"),
        ("+10", "Plus de 10 ans"),
    )

    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=60, unique=True,
                             **NULL_AND_BLANK,)
    title = models.CharField(max_length=120, **NULL_AND_BLANK)
    address = models.CharField(max_length=120, **NULL_AND_BLANK)
    experience = models.CharField(
        max_length=60, choices=EXPERIENCE_CHOICES, **NULL_AND_BLANK)
    skills = models.ManyToManyField("job.Skills")
    description = models.TextField(
        verbose_name="description",
        max_length=300,
        help_text="Write your biography in 300 words.",
        **NULL_AND_BLANK
    )
    avatar = models.ImageField(
        verbose_name="avatar",
        upload_to="avatars/%Y/%m%d",
        **NULL_AND_BLANK
    )
    resume = models.FileField(
        verbose_name="resume",
        upload_to="cvs/%Y/%m%d",
        **NULL_AND_BLANK
    )
    is_investor = models.BooleanField(
        verbose_name="investor",
        default=False,
        help_text="Are you an investor ?"
    )
    is_project_owner = models.BooleanField(
        verbose_name="project owner",
        default=False,
        help_text="Are you a project owner ?"
    )
    is_job_seeker = models.BooleanField(
        verbose_name="job seeker",
        default=False,
        help_text="Are you a job seeker ?"
    )
    is_recruiter = models.BooleanField(
        verbose_name="company",
        default=False,
        help_text="Are you a company ?"
    )
    company = models.CharField(
        verbose_name="comapny name",
        max_length=180, null=True
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )

    class Meta:
        ordering = ['-date_joined']

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return "https://via.placeholder.com/251x296"

    def _get_unique_slug(self):
        slug = slugify(self.email.split("@")[0])
        unique_slug = slug
        num = 1
        while CustomUser.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
