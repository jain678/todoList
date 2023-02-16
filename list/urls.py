from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoView.as_view()),
    path('<int:pk>/', TodoView.as_view()),
    path('mark_as_done/<int:pk>/',MarkdoneAPIView.as_view()), # To mark the task as complete/incomplete

]