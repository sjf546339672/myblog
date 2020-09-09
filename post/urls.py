# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("", views.queryAll, name="queryAll"),
    path("page/<str:num>/", views.queryAll),
    path("post/<int:id>/", views.detail, name="detail"),
    path('category/<int:id>/', views.queryPostByCid),
    path('archive/<str:year>/<str:month>/', views.queryPostByCreated),
]




