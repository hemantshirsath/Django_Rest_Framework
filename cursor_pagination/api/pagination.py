from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size=3
    ordering='-name'