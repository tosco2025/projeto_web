from django.urls import path
from . import views

urlpatterns = [
    path('projeto/', views.index, name='index'),
]