from django.urls import path
from . import views

urlpatterns = [
    path("", views.training_list, name="list"),                  # /trainings/
    path("<slug:slug>/", views.training_detail, name="detail"),  # /trainings/<slug>/
]