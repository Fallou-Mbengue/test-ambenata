from django.db import models


class BaseTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class Contact(BaseTimeStampedModel):
    name = models.CharField(
        verbose_name="Name",
        max_length=30)
    email = models.EmailField(
        verbose_name="Email",
    )
    phone = models.CharField(
        verbose_name="Phone",
        max_length=40)
    subject = models.CharField(
        verbose_name="Subject",
        max_length=60)
    message = models.TextField(
        verbose_name="your message",
        max_length=100)

    def __str__(self):
        return self.name
