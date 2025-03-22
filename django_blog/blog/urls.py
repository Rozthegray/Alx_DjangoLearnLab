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


from django.urls import path
from .views import search_posts

urlpatterns = [
    path('search/', search_posts, name='search-posts'),
]


urlpatterns = [
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]
