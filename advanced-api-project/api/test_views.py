from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test client, create user, and seed test data."""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2024)

        self.valid_book_data = {"title": "New Book", "author": self.author.id, "publication_year": 2023}
        self.invalid_book_data = {"title": "", "author": self.author.id, "publication_year": 2025}

    def test_get_books_list(self):
        """Test retrieving a list of books."""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        """Test authenticated user can create a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Test unauthenticated user cannot create a book."""
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test authenticated user can update a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f"/api/books/update/{self.book.id}/", {"title": "Updated Book", "author": self.author.id, "publication_year": 2022}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Test authenticated user can delete a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
