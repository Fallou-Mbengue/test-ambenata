from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from project.forms import ProjectPostForm
from django.contrib.messages.views import SuccessMessageMixin


# from project.models import Project
from dash import mixins
from project import models, forms
from user.forms import UserUpdateForm


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
    return render(request, "dash/project_owner/index.html", {"form": form})


class Project_OwnerView(TemplateView):
    template_name = "dash/project_owner/profile.html"


class ProjectListView(ListView):
    model = models.Project
    paginate_by = 10
    context_object_name = "projects"
    template_name = "dash/project_owner/list_projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = models.Project.objects.filter(
            user__id=self.request.user.id)
        return context
    

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = "dash/project_owner/detail_project.html"
   


class ProjectCreateView(SuccessMessageMixin,mixins.ProjectOwnerMixin, CreateView):
    model = models.Project
    form_class = ProjectPostForm
    template_name = "dash/project_owner/create_project.html"


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = ProjectPostForm
    template_name = "dash/project_owner/create_project.html"


class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = "dash/project_owner/delete_project.html"

    def get_seccess_url(self):
        return reverse('dashboard:project_owner_delete_project')


class DashView(TemplateView):
    template_name = "dash/project_owner/dashboard.html"

