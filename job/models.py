# job.models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from page.models import BaseTimeStampedModel


NULL_AND_BLANK = {'null': True, 'blank': True}


class Category(BaseTimeStampedModel):

    title = models.CharField(
        verbose_name="category title",
        max_length=25
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Catégories d'emploi"

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


class Offer(BaseTimeStampedModel):

    OFFER_CHOICES = (
        ('Examen', 'Examen'),
        ('Devoir', 'Devoir'),
    )

    EDUCATION_CHOICES = (
        ('L1-GI', 'L1-GI'),
        ('L2-GI', 'L2-GI'),
        ('L3-GI', 'L3-GI'),
    )

    user = models.ForeignKey(
        "user.CustomUser",
        limit_choices_to={
            'is_recruiter': True,
            'is_active': True
        },
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name="Donner un titre",
        max_length=180, null=True
    )
    content = models.TextField(
        verbose_name="donner une description",
        null=True
    )
    document_desc = models.FileField(
        verbose_name="document",
        upload_to="career/",
        **NULL_AND_BLANK
    )
    date_validation = models.DateTimeField(
        verbose_name="Date limite", auto_now=False,
        auto_now_add=False
    )
    # category = models.ForeignKey(
    #     to=Category,
    #     verbose_name="catégorie d'emploi",
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    offer_type = models.CharField(
        verbose_name="type d'offre",
        choices=OFFER_CHOICES,
        default="Examen",
        max_length=180, null=True
    )
    education_level = models.CharField(
        choices=EDUCATION_CHOICES,
        default="L1-GI",
        verbose_name="Classe",
        max_length=180, null=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="publier"
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Offres d'emplois"

    def __str__(self):
        return f"{self.user.company} - {self.title}"

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Offer.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def apply_jobs(self):
        return Apply.objects.filter(offer=self)

    def get_offer_update_url(self):
        return reverse(
            "dashboard:recruiter_update_offer",
            kwargs={"pk": self.id}
        )

    def get_offer_delete_url(self):
        return reverse(
            "dashboard:recruiter_delete_offer",
            kwargs={"pk": self.id}
        )


class Apply(BaseTimeStampedModel):
    STATUS_CHOICES = (
        ('Seen', 'Vue'),
        ('Rejected', 'Rejeté'),
        ('Accepted', 'Accepté')
    )
    candidate = models.ForeignKey(
        "user.CustomUser",
        limit_choices_to={
            'is_job_seeker': True,
            'is_active': True
        },
        verbose_name="candidats",
        on_delete=models.SET_NULL,
        null=True,
        related_name="applied_job",
    )
    offer = models.ForeignKey(
        "job.Offer",
        verbose_name="offers",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=30, null=True
    )

    def __str__(self):
        return f"{self.offer} {self.candidate} {self.status}"

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Candidatures"


class Skills(BaseTimeStampedModel):

    title = models.CharField(
        verbose_name="Skills title",
        unique=True,
        max_length=180
    )
    slug = models.SlugField(
        unique=True,
        **NULL_AND_BLANK
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Skills"

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Skills.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Experience(BaseTimeStampedModel):

    user = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        limit_choices_to={
            'user__is_job_seeker': True,
            'is_active': True
        },
        verbose_name="job seeker",
        related_name="experiences",
    )

    title = models.CharField(
        verbose_name="title",
        max_length=200,
        null=True
    )
    subtitle = models.CharField(
        verbose_name="sub-title",
        max_length=200,
        null=True
    )
    description = models.TextField(
        verbose_name="description"
    )
    project_url = models.URLField(
        verbose_name="project url",
        default="https://www.myproject.com/",
        max_length=250,
        **NULL_AND_BLANK
    )
    begin_date = models.DateField(
        verbose_name="begin date",
        **NULL_AND_BLANK
    )
    end_date = models.DateField(
        verbose_name="begin end",
        **NULL_AND_BLANK
    )

    def __str__(self) -> str:
        return self.title


class Certificate(BaseTimeStampedModel):
    user = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        limit_choices_to={
            'user__is_job_seeker': True,
            'is_active': True
        },
        verbose_name="job seeker",
    )
    title = models.CharField(
        verbose_name="certificate name",
        max_length=200,
        **NULL_AND_BLANK
    )
    description = models.CharField(
        verbose_name="certificate description",
        max_length=500, **NULL_AND_BLANK
    )
    issuer = models.CharField(
        verbose_name="certificate issuer name",
        max_length=200,
        **NULL_AND_BLANK
    )
    issue_date = models.DateField(
        verbose_name="certificate issue date",
        **NULL_AND_BLANK
    )
    expiration_date = models.DateField(
        verbose_name="expiration date",
        **NULL_AND_BLANK
    )
    url = models.URLField(
        verbose_name="certificate url",
        **NULL_AND_BLANK
    )
    is_active = models.BooleanField(
        verbose_name="certificate is active",
        default=True
    )

    def __str__(self) -> str:
        return self.title
