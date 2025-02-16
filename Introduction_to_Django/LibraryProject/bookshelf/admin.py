from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Display fields in the admin list view
    list_filter = ("publication_year", "author")  # Filter books by year and author
    search_fields = ("title", "author")  # Enable search by title and author

admin.site.register(Book, BookAdmin)
