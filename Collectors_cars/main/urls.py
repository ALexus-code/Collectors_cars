from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('about', views.about,  name='about'),
    path('create', views.create,  name='create'),
    path('register/', views.Register.as_view(), name='register'),
]