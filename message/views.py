# message.views.py
from django.db.models import Count
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect

from dash import mixins
from message import models, forms
from message.models import Chat


class CreateDialogView(mixins.DispatchRecruiterMixin, generic.View):
    def get(self, request, user_id):
        chats = (
            models.Chat.objects.filter(
                members__in=[request.user.id, user_id], type=Chat.DIALOG
            )
            .annotate(c=Count("members"))
            .filter(c=2)
        )

        if chats.count() == 0:
            chat = models.Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse("users:messages", kwargs={"chat_id": chat.id}))


create_dialogue_view = CreateDialogView.as_view()


class DialogueView(mixins.DispatchRecruiterMixin, generic.View):
    template_name = "dash/message/dialogue.html"

    def get(self, request, *args, **kwargs):

        chats = models.Chat.objects.filter(members__in=[request.user.id])
        context = {"chats": chats, "page_title": "messages", "profile": request.user}
        return render(request, self.template_name, context)


dialogue_view = DialogueView.as_view()


class MessagesView(mixins.DispatchRecruiterMixin, generic.View):
    form_class = forms.MessageForm
    template_name = "dash/message/message_list.html"

    def get(self, request, chat_id, *args, **kwargs):
        form = self.form_class()
        try:
            chat = models.Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(
                    author=request.user
                ).update(is_readed=True)
            else:
                chat = None
        except models.Chat.DoesNotExist:
            chat = None

        context = {
            "chats": chat,
            "form": form,
            "page_title": "message",
            "profile": request.user,
        }
        return render(request, self.template_name, context)

    def post(self, request, chat_id):
        form = self.form_class(data=request.POST or None)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()

        return redirect(
            reverse("dashboard:recruiter_message", kwargs={"chat_id": chat_id})
        )


message_view = MessagesView.as_view()
