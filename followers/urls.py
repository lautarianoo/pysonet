from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListFollowerView.as_view()),
    path('<int:pk>', views.FollowerView.as_view())
]