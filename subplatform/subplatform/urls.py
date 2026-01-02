from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls", namespace="account")),
    #path("client/", include("client.urls", namespace="client")),
    #path("writer/", include("writer.urls", namespace="writer")),
    path("client/", include("client.urls")),
    path("writer/", include("writer.urls")),
]
