from django.urls import path, include
from projects import views

urlpatterns = [
    path('' , views.get_projects),
]