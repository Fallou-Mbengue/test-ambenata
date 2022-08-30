from django.contrib import messages
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from user.forms import UserUpdateForm
from user.models import CustomUser
from project.models import FollowedProject, Project


@login_required
def dashboard(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Information mise a jour avec succes")
            return redirect("dashboard:dashboard")
        else:
            messages.error(request, f"{form.errors}")
            return redirect("dashboard:dashboard")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "dash/investor/index.html", {"form": form})


class DashView(TemplateView):
    template_name = "dash/investor/dashboard.html"


@login_required
def favorite_ajax(request):
    data = {"success ": False}
    if request.is_ajax():
        projet_id = request.POST["projects"]
        projet = get_object_or_404(Project, pk=int(projet_id))
        investisseur = CustomUser.objects.create(
            project=projet, investis=request.user
        )
        print(investisseur)
    data = {"success": True}
    return JsonResponse(data)


@login_required
def followed_project(request):
    followeds = FollowedProject.objects.filter(
        investor=request.user
    )
    return render(request, "dash/investor/followed_project.html", {"followeds": followeds})
