from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from django.http import Http404
import json
from books.models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import ReviewForm
from django.core.files.storage import FileSystemStorage

# with open('C:\work\pythonwork\Environments\\books.json') as f:
#    booksData = f.read()

# print(type(booksData))
#data = json.loads(booksData)

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    #template_name = 'books/index.html'
    #context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    """
    This method needs to write because we need order by records
    We overwrite this DetailView method.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
        return context


def review(request, id):
    if request.user.is_authenticated:
        body = request.POST['body']
        #book_id = request.POST['id']
        newReview = Review(body=body, book_id=id, user=request.user)

        print('Length of len(request.FILES): ', len(request.FILES))
        # if len(request.FILES) != 0:
        image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(image.name, image)
        newReview.image = fs.url(name)
        print(newReview.image)
        newReview.save()
    return redirect(f'/book/{id}')


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)
