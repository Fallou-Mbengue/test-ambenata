import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_good_home(client):
    url = reverse("page:home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_good_contact(client):
    url = reverse("page:contact_form")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_good_about(client):
    url = reverse("page:about")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_404_home(client):
    url = "/normally404"
    response = client.get(url)
    assert response.status_code == 404
