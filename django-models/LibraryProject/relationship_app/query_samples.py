from relationship_app.models import Author, Book, Library, Librarian

def query_examples():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian of {library_name}: {librarian.name}")

# Run query_examples in Django shell
# python manage.py shell
# >>> from relationship_app.query_samples import query_examples
# >>> query_examples()
