from django.urls  import path
from . import views


urlpatterns = [
    path('',views.BookListView.as_view(), name='index'),
    #path('',views.index, name='index'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book.show'),
    #path('<int:id>', views.show, name='book.show'),
    path('<int:id>/review', views.review, name='book.review'),
    path('<str:author>/books', views.author, name='author.books')
] 
