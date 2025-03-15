from rest_framework import viewsets  # ✅ Ensure this is imported
from .models import Book
from .serializers import BookSerializer

# ✅ Define the BookViewSet using ModelViewSet
class BookViewSet(viewsets.ModelViewSet):  
    """
    A ViewSet for performing CRUD operations on Book model.
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
