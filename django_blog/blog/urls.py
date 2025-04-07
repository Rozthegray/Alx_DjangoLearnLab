from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView
)
from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]


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
