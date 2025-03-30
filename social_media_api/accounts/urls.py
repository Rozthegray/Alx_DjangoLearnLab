from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Explicit register route
    path('login/', ObtainAuthToken.as_view(), name='login'),  # Explicit login route
    path('profile/', ProfileView.as_view(), name='profile'),  # Profile management route
]
