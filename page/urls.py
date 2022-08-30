# pages.urls.py

from django.urls import path
from .views import contacts, home, about

app_name = "page"
urlpatterns = [
    path("",home,name="home",),
    path("contact/", contacts, name="contacts"),
    path("about/", about, name="about"),
]
