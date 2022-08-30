import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_good_project(client):
    url = reverse("project:list-projets")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def tes_good_favorit(client):
    url = reverse("project:new-favorit")
    response = client.get(url)
    assert response.status_code == 200
