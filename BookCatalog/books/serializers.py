# books/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # Add 'availability' back to the list of fields
        fields = ['id', 'title', 'author', 'genre', 'publication_year', 'availability']