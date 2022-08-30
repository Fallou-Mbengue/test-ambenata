# project.urls.py

from django.urls import path
from project.views import ProjectList, new_favorit


def test_project(request):
    return 123


app_name = 'project'
urlpatterns = [
    path("test/project/", test_project),
    path("", ProjectList.as_view(), name="list-projets"),
    path("favorite/<int:investor_id>/<int:project_id>/", new_favorit, name="new-favorit")
]
