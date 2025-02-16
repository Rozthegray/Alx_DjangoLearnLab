# Delete a Book Instance

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully!")
