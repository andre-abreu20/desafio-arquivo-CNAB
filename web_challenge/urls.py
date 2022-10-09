from django.urls import path

from . import views

urlpatterns = [
    path("", views.FormCNAB.as_view(), name="index"),
    path("documentation/", views.DocumentationList.as_view(), name="doc")
]
