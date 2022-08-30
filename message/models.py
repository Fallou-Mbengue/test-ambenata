# message.models.py

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from page.models import BaseTimeStampedModel


NULL_AND_BLANK = {'null': True, 'blank': True}


class Chat(BaseTimeStampedModel):
    
    DIALOG = 'D'
    CHAT = 'C'

    CHAT_TYPE_CHOICES = (
        (DIALOG, "Dialogue"),
        (CHAT, "Chat")
    )
 
    type = models.CharField(
        verbose_name='type de chat',
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(
        to=get_user_model(),
        verbose_name="Membres"
    )

    class Meta:
        ordering = ["created"]
        get_latest_by = ['created']
        verbose_name_plural = 'chats'
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.type
 
    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk }


class Message(BaseTimeStampedModel):
    
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.SET_NULL,
        verbose_name='chat',
        null=True
    )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name='auteur',
        null=True
    )
    message = models.TextField(
        verbose_name='message',
        help_text='message'
    )
    is_readed = models.BooleanField(
        verbose_name="message lu",
        default=False
    )

    class Meta:
        ordering = ["created"]
        get_latest_by = ['created']
        verbose_name_plural = 'messages'
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return f"Message de {self.author.email}"
