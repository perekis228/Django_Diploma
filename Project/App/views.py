from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def books(request):
    books = Book.objects.all().order_by('title')
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Список книг',
        'books': books,
        'page_obj': page_obj
    }
    return render(request, 'books.html', context)

def book_watch(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'book_watch.html', {'book': book})