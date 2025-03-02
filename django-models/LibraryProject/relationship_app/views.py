from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView  # ✅ Using DetailView for class-based view
from .models import Book, Library  # ✅ Ensuring Library is imported

# ✅ Function-Based View for Listing All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# ✅ Class-Based View for Displaying Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
