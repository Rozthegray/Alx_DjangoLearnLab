from django.urls import path, include
from rest_framework.routers import DefaultRouter  # ✅ Make sure this is imported
from .views import BookViewSet, BookList

# ✅ Create a router instance
router = DefaultRouter()

# ✅ Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing endpoint for listing books
    path('books/', BookList.as_view(), name='book-list'),
    
    # ✅ Include router-generated URLs
    path('', include(router.urls)),  
]
