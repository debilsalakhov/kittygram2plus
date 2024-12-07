from rest_framework.pagination import PageNumberPagination


class CatPagination(PageNumberPagination):
    page_size = 20
