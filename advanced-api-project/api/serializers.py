from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)  # Shows book titles in Author API

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'books']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)  # Include author's name

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'genre']
