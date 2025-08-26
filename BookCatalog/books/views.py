from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
        else:
            books = self.get_queryset()

        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

# Create your views here.
