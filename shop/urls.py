from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/fish', views.fish),
    path('/plants', views.plants),
    path('aboutus/', views.aboutus, name='home'),
    path('contact/', views.contact, name='home')
]
