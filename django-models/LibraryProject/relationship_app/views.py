from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Explicitly included Library

# ✅ Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Fixed template reference

# ✅ Class-based view for displaying library details and listing its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ Correct template reference
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # ✅ Lists all books in the library
        return context
