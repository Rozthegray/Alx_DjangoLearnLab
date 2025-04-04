# posts/urls.py
from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    # Like post
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),

    # Unlike post
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
