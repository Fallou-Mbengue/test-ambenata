from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView

from user.models import CustomUser
from user.forms import UserUpdateForm


@login_required
def dashboard(request):
    candidates = CustomUser.objects.candidates().count()
    recruiters = CustomUser.objects.recruiters().count()
    project_owners = CustomUser.objects.project_owners().count()
    investors = CustomUser.objects.investors().count()
    context = {
        "candidates": candidates,
        "recruiters": recruiters,
        "project_owners": project_owners,
        "investors": investors,
    }
    return render(request, "dash/staff/index.html", context)


@login_required
def settings(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Information mise a jour avec succes")
            return redirect("dashboard:staff_settings")
        else:
            messages.error(request, f"{form.errors}")
            return redirect("dashboard:staff_settings")
    else:
        form = UserUpdateForm(instance=user)

    template = "dash/staff/settings.html"
    context = {"form": form, "page_title": "paramètre"}

    return render(request, template, context)


class CandidateListView(ListView):
    paginate_by = 10
    context_object_name = "candidates"
    template_name = "dash/staff/candidate_list.html"

    def get_queryset(self, **kwargs):
        return CustomUser.objects.candidates()


class RecruiterListView(ListView):
    paginate_by = 10
    context_object_name = "recruiters"
    template_name = "dash/staff/recruiter_list.html"

    def get_queryset(self, **kwargs):
        return CustomUser.objects.recruiters()


class InvestorListView(ListView):
    paginate_by = 10
    context_object_name = "investors"
    template_name = "dash/staff/investor_list.html"

    def get_queryset(self, **kwargs):
        return CustomUser.objects.investors()


class ProjectOwnerListView(ListView):
    paginate_by = 10
    context_object_name = "project_owners"
    template_name = "dash/staff/project_owner_list.html"

    def get_queryset(self, **kwargs):
        return CustomUser.objects.project_owners()
