from django.urls import include, path
from . import views
from .views import post_list

urlpatterns = [
    path('', views.post_list, name='post_list'),
]