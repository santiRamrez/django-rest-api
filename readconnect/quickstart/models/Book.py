from django.db import models

from .Author import Author
from .Category import Category

class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    imgURI = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=20, null=True)
    shortDescrip = models.TextField(null=True)
    longDescrip = models.TextField(null=True)
    pageCount = models.IntegerField(null=True)
    publishedDate = models.DateTimeField(null=True)
    categories = models.ManyToManyField(Category, db_table="book_categories")
    authors = models.ManyToManyField(Author, db_table="book_authors")
    avgEvaluation = models.DecimalField(decimal_places=1, max_digits=1, null=True)

    def __str__(self):
        return f'{self.title} - {self.authors}'