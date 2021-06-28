from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Authors)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.pk} {self.title}"


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    #book_id = models.BigIntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True)

