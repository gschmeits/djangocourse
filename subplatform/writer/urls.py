from django.urls import path
from . import views

#app_name = "writer"

urlpatterns = [
    path("writer-dashboard/", views.writer_dashboard, name="writer-dashboard"),
]
