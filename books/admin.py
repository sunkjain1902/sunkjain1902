from django.contrib import admin
from books.models import Book, Review, Authors
# Register your models here.

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Authors)