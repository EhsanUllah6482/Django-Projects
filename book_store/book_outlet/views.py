from django.shortcuts import render
from .models import Book,Author
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all()
    Book.objects.create(title="Harry Potter",rating=5,is_bestseller=True,slug="harry-potter-1",author="j.krollings")

    avg_rating=books.aggregate(Avg("rating"))
    return render(
        request,
        "index.html",
        {
            "books": books,
            "total_books": books.count(),
            "average_rating": avg_rating
            , 
        },
    )


def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404("Book not found")
    return render(
        request,
        "book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestseller,
        },
    )
