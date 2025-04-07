from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView
)


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
