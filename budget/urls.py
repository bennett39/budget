from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('two-factor', views.two_factor, name='two-factor'),
]
