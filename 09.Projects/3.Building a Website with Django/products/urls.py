from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Maps the root url to that function in the module
    path('new', views.new)
]