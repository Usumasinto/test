from django.urls import path

from zones.api import views

urlpatterns = [
    path('edit-update/', views.edit),
    path('delete-zone/<str:pk>', views.deleteZone),




]
