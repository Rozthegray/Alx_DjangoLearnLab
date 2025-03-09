from django.shortcuts import render
from .forms import ExampleForm
from .models import Book  # Assuming you have a Book model

# View for the form example
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data (you can save it to the database or perform some other action)
            form_data = form.cleaned_data
            return render(request, 'bookshelf/example_success.html', {'form_data': form_data})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# View for the book list
def book_list_view(request):
    books = Book.objects.all()  # Assuming you have a Book model with fields like 'title' and 'author'
    return render(request, 'bookshelf/book_list.html', {'books': books})
