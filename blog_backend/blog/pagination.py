from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size = 5   # default page size
    page_size_query_param = 'size'  # ?page=xx&size=??
    max_page_size = 100 # max page size
