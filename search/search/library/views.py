from django.shortcuts import render
from .models import Book
from boyermoore import search_file

def home(request):
    query = request.GET.get('query')
    books = []

    if query:
        # Search for query words within the database fields
        books = Book.objects.filter(title__icontains=query) | \
                Book.objects.filter(description__icontains=query) | \
                Book.objects.filter(author__icontains=query) | \
                Book.objects.filter(isbn__icontains=query)

    return render(request, 'home.html', {'books': books, 'query': query})
