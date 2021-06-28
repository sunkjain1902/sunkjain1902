from django.shortcuts import render, get_object_or_404, redirect 
#from django.http import HttpResponse
from django.http import Http404
import json
from books.models import Book, Review

with open('C:\work\pythonwork\Environments\\books.json') as f:
    booksData = f.read()

print(type(booksData))
data = json.loads(booksData)

# Create your views here.

def index(request):
    #context = {'name' : 'Sunil'}
    """ context = { "book" : 
        {
            "title": "Unlocking Android",
            "thumbnailUrl": "https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ableson.jpg"
        }
    } """
    dbData = Book.objects.all()
    #print(dbData)
    context = {
        "books" : dbData
    }
    return render(request, 'books/index.html', context)
    #return render(request, 'books/index.html')
    #return render(request, 'index.html')
    #return HttpResponse('Hello Books App')

def show(request, id):
    #singleBook = Book.objects.get(pk=id)
    #singleBook = Book.objects.filter(id=id).first()
    """   try:
        singleBook = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found') """
    singleBook = get_object_or_404(Book,pk=id)
    """  singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book """
    #reviews = Review.objects.all()
    #reviews = Review.objects.order_by('-created_at')
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    context = { "book" : singleBook, 'reviews':reviews }
    return render(request, 'books/show.html', context)

def review(request, id):
    review = request.POST['review']
    #book_id = request.POST['id']
    newReview = Review(body=review, book_id=id)
    newReview.save()
    return redirect('/book')