from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListFollowerView.as_view()),
    path('add/', views.AddFollowerView.as_view())
]