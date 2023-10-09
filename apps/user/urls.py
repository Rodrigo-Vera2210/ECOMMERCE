from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('crear/', UserCreate.as_view()),
    path('vista/<id>', UserView.as_view()),
]
