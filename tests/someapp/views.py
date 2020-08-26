# Create your views here.
from .models import Book


def get_books(request):
    return render('someapp/books.html', request, {'books': Book.nodes.all()})
