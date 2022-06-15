from django.urls import path
from . import views

urlpatterns = [
    path('imust/', views.imust),  # IMUST大事日历
]
