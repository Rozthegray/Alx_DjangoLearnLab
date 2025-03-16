from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'publication_year']

    def validate_title(self, value):
        """Ensure the title is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # ✅ Fixing the error

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'books']
