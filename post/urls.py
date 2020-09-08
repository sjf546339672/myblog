# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("", views.queryAll, name="queryAll"),
    path("page/<str:num>/", views.queryAll),
    path("post/<str:id>/", views.detail, name="detail"),
]




