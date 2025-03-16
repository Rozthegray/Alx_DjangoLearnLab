from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre']

    def validate_title(self, value):
        """Ensure the title is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value
