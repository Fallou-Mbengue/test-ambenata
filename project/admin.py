from django.contrib import admin
from .models import Category, Project, FollowedProject

# admin.site.register(Project)
admin.site.register(Category)
# admin.site.register(FollowedProject)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "budget", "user"]


@admin.register(FollowedProject)
class FollowedProjectAdmin(admin.ModelAdmin):
    list_display = ["project", "investor",]
    

    
        
