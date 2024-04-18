from django.urls import path
from .views import *
urlpatterns = [
    path('',HelloView.as_view()),
    path('api/login', login)
]