from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # ✅ Import the built-in view
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# ✅ Set up the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # ✅ Include the router
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # ✅ Add the token auth route
]
