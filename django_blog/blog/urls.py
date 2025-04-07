from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView
)
from django.urls import path
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    # Existing URLs...
    
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]


urlpatterns = [
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
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
