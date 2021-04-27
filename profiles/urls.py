from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', UserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
]