from django.urls import path
from . import views

urlpatterns = [
    path("", views.complete_task),
    path("add/", views.add_task)
]