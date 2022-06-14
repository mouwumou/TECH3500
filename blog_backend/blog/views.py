from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer
from .pagination import BlogPagination

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend,]
