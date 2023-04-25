from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("delux/", views.delux, name="delux"),
    path("packages/", views.restaurant, name="restaurant"),
    path("Activities & Services/", views.Services, name="Services"),
    path("gallery", views.gallery, name="gallery"),
    

]