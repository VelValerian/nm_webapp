from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),                         # Главная
    path("about/", views.about, name="about"),                  # Про Меня
    path("corporate/", views.corporate, name="corporate"),      # Корпоративные тренировки
    path("contacts/", views.contacts, name="contacts"),         # Контакты
]