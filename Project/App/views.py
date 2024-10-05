from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import *
from .models import *

user = None
# Create your views here.
def registration(request):
    users = User.objects.all()
    info = {'error': []}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if password != repeat_password:
                info['error'].append('Пароли не совпадают')
            for user in users:
                if username == user.username:
                    info['error'].append('Пользователь уже существует')
                    break
            if not info['error']:
                User.objects.create(username=username, password=password, age=age)
                return books(request)
    else:
        form = UserRegister()
    context = {'form': form, 'errors': info['error']}
    return render(request, 'registration.html', context)

def log_in(request):
    info = {'error': []}
    if request.method == 'POST':
        form = UserLogIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            global user
            user = User.objects.get(username=username)
            if not user:
                info['error'].append('Такого пользователя не существует')
            elif user.password != password:
                info['error'].append('Неверный пароль')

            if not info['error']:
                return redirect('/books')
    else:
        form = UserLogIn()
    context = {'form': form, 'errors': info['error']}
    return render(request, 'log_in.html', context)

def books(request):
    books = Book.objects.all().order_by('title')
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']
            description = form.cleaned_data['description']
            Book.objects.create(title=title, author=author, description=description, genre=genre)
            return redirect('/books')
    else:
        form = CreateBook()

    if request.method == 'GET':
        filter_by = request.GET.get('filter')
        if filter_by:
            books = Book.objects.all().order_by(filter_by)
    paginator = Paginator(books, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    global user
    context = {
        'title': 'Список книг',
        'form': form,
        'books': books,
        'page_obj': page_obj,
        'user': user
    }
    return render(request, 'books.html', context)

def book_watch(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'book_watch.html', {'book': book})