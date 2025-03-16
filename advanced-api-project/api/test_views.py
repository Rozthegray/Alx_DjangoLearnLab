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
        self.assertGreater(len(response.data), 0)  # Ensure at least one book exists
        self.assertEqual(response.data[0]["title"], self.book.title)  # Check expected title

    def test_login_required_for_create(self):
        """Test that a user must be logged in to create a book."""
        # Try creating a book without logging in
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Now log in using session-based authentication
        login_success = self.client.login(username="testuser", password="password")
        self.assertTrue(login_success)  # Ensure login was successful

        # Retry creating a book after login
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")  # Ensure correct title

    def test_create_book_authenticated(self):
        """Test authenticated user can create a book using token-based auth."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        """Test authenticated user can update a book."""
        self.client.force_authenticate(user=self.user)
        updated_data = {"title": "Updated Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.put(f"/api/books/update/{self.book.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Test authenticated user can delete a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to retrieve deleted book
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Ensure it's deleted
