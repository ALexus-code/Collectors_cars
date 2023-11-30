from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('about', views.about,  name='about'),
    path('create', views.create,  name='create'),
    path('register/', views.Register.as_view(), name='register'),
    #path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    #path('', views.PostListView.as_view()),
]