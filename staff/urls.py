from django.urls import path
from staff import views

app_name = "staff"

urlpatterns = [
   path("", views.index, name="index"),
   path("login/", views.login, name="login"),
   path("logout/", views.logout, name="logout"),
]