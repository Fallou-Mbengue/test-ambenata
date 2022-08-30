import pytest

from project.models import Project, Category


@pytest.mark.djnago_db
# def test_create_project():
    #category = Category.objects.create(title="category title")
    # project = Project.objects.create(
    #title="titre projet",
    #resume="resume projet",
    #description="description projet",
    # budget=10000,
    # )
    #assert project.title == "titre projet"
    #assert category.title == "category title"


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(title="creation category test")
    assert category.title == "creation category test"
