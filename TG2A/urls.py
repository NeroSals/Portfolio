from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("TG2A", views.tg2a, name="TG2A"),
    path("TG2A/add", views.add_image, name="add_image"),
    path("gallery/<img_id>", views.image_page, name="image_page")
    ]