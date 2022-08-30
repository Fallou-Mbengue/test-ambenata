from django.urls import reverse
from django.contrib import admin

from message.models import Chat, Message


admin.site.register(Chat)
admin.site.register(Message)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_per_page = 10
    list_filter = ["author"]
    list_display = ['author', 'message']
    list_display_links = ['author']
