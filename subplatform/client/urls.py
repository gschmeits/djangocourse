from django.urls import path
from . import views

#app_name = "client"

urlpatterns = [
    path('client-dashboard/', views.client_dashboard, name='client-dashboard'),
]
