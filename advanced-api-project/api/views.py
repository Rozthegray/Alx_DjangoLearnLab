from rest_framework import generics, filters
from django_filters import rest_framework as django_filters  # ✅ Add this line
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Add Filtering, Searching, and Ordering
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Enable filtering by title, author, and publication_year
    filterset_fields = ['title', 'author__name', 'publication_year']

    # ✅ Enable search functionality on title and author fields
    search_fields = ['title', 'author__name']

    # ✅ Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
