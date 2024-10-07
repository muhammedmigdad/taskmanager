from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
    path("", views.index, name="index"),
    path('verified/<int:id>/', views.item_verified, name='item_verified'),
    path("unauthorized_access/", views.unauthorized_access, name="unauthorized_access"),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),


]