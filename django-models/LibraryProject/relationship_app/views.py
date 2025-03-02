from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Explicitly added Library

# ✅ Function-based view for listing books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Explicitly included

# ✅ Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ Explicitly included
    context_object_name = "library"
