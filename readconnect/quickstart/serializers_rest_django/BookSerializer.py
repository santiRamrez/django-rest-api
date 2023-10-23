from rest_framework import serializers

from ..models.Book import Book

class BookListSerializer(serializers.ListSerializer):
    #This is a more efficient way to add a list of objects into the database
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'