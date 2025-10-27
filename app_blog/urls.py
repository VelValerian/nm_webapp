from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="list"),                # /blog/
    path("<slug:slug>/", views.post_detail, name="detail") # /blog/<slug>/
]