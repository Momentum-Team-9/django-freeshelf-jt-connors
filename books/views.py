from django.shortcuts import render
from .models import User, Book, Category

# Create your views here.

from django.shortcuts import render
from .models import Book, Category
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def homepage(request):
    return render(request, "books/index.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def show_category(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    books = categories.books.all()

    return render(request, "books/category.html", {"categories": categories, "books": books})