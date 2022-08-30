from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from user.models import CustomUser
from .models import FollowedProject, Project

# Create your views here.

class ProjectList(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "project/list-projets.html"
    
def new_favorit(request, investor_id, project_id):
    investor = get_object_or_404(CustomUser, pk=int(investor_id))
    project = get_object_or_404(Project, pk=int(project_id))
    
    favorite = FollowedProject.objects.filter(
        project__id=project.id, investor__id=investor.id)
    if favorite.exists():
        messages.error(request, "Ce projet existe déja dans votre liste de favorite")
        return redirect("dashboard:project_owner_detail", slug=project.slug)
    else:
        FollowedProject.objects.create(project=project, investor=investor)
        # redirection vers la liste des projets favorite
        messages.success(request, "Le projet à était ajouter au liste favorite avec succée ")
        return redirect("dashboard:followed_project")    
    
